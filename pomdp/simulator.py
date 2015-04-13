#!/usr/bin/env python

import sys
import time
import pomdp_parser
import policy_parser
import speech_recognizer
import numpy
import random
from scipy import stats
sys.path.append('/home/szhang/software/python_progress/progress-1.2')
from progress.bar import Bar
import subprocess

class Simulator(object):

  def __init__(self, 
               policy_file_full='policy/default.policy', 
               pomdp_file='models/default.pomdp', 
               auto_observations=True,
               uniform_init_belief =True,
               print_flag=True,
               actual_time='day',
               robot_time='day',
               policy_switch='pomdp',
               trials_num=1000,
               min_cost=0,
               max_cost=1000,
               rounds=1, 
               num_item=1, 
               num_person=1,
               num_room=1):
    self.auto_observations = auto_observations
    self.uniform_init_belief = uniform_init_belief
    self.print_flag = print_flag
    self.policy_switch = policy_switch
    self.trials_num = trials_num
    self.rounds = rounds

    print(pomdp_file)
    print(policy_file_full)

    self.policy_file_full = policy_file_full
    self.min_cost = min_cost
    self.max_cost = max_cost

    self.num_item = num_item
    self.num_person = num_person
    self.num_room = num_room

    model = pomdp_parser.Pomdp(filename=pomdp_file, parsing_print_flag=True)
    self.states = model.states
    self.actions = model.actions
    self.observations = model.observations
    self.trans_mat = model.trans_mat
    self.obs_mat = model.obs_mat
    self.reward_mat = model.reward_mat

    self.b = None
    self.a = None
    self.o = None
    self.r = 0.0
    self.actual_time = actual_time
    self.robot_time = robot_time

    self.pk_mor = [\
      0.072, 0.006, 0.006, 0.009, 0.006, 0.072, 0.006, 0.009, 0.00133333,
      0.00133333, 0.016, 0.002, 0.288, 0.024, 0.024, 0.021, 0.024, 0.288, 0.024,
      0.021, 0.00533333, 0.00533333, 0.064, 0.00466667]

    self.pk_noo = [\
      0.206452, 0.0172043, 0.0172043, 0.0172043, 0.0172043, 0.206452, 0.0172043,
      0.0172043, 0.0172043, 0.0172043, 0.206452, 0.0172043, 0.0516129,
      0.00430108, 0.00430108, 0.0150538, 0.00430108, 0.0516129, 0.00430108,
      0.0150538, 0.00430108, 0.00430108, 0.0516129, 0.0150538]
    self.pk_aft = [\
      0.04, 0.00333333, 0.00333333, 0.0025, 0.00333333, 0.04, 0.00333333,
      0.0025, 0.02, 0.02, 0.24, 0.015, 0.06, 0.005, 0.005, 0.00583333, 0.005,
      0.06, 0.005, 0.00583333, 0.03, 0.03, 0.36, 0.035]

    self.pk_day = [\
      0.109491, 0.00912429, 0.00912429, 0.00982246, 0.00912429, 0.109491,
      0.00912429, 0.00982246, 0.0129911, 0.0129911, 0.155893, 0.0115947,
      0.130487, 0.0108739, 0.0108739, 0.0139987, 0.0108739, 0.130487, 0.0108739,
      0.0139987, 0.0129147, 0.0129147, 0.154976, 0.018134]

    self.pk_day = numpy.ones((1,len(self.states))) / float(len(self.states))

    if self.actual_time is 'morning':
      self.pk = self.pk_mor
    elif self.actual_time is 'noon':
      self.pk = self.pk_noo
    elif self.actual_time is 'afternoon':
      self.pk = self.pk_aft
    elif self.actual_time is 'day':
      self.pk = self.pk_day
    else:
      print('Something wrong happened')
      sys.exit()


    self.policy_full = policy_parser.Policy(len(self.states), len(self.actions), 
                                       filename=self.policy_file_full)

    numpy.set_printoptions(precision=3)

  #######################################################################
  def init_belief(self):
    if self.uniform_init_belief:
      self.b = numpy.ones((len(self.states), 1, )) / len(self.states)
      self.b = self.b.T
    # the following code will go wrong, as the pk_xxx's wrong size
    elif self.robot_time is 'morning':
      self.b = numpy.matrix(self.pk_mor)
    elif self.robot_time is 'noon':
      self.b = numpy.matrix(self.pk_noo)
    elif self.robot_time is 'afternoon':
      self.b = numpy.matrix(self.pk_aft)
    elif self.robot_time is 'day':
      self.b = numpy.matrix(self.pk_day)
    else:
      print('Something wrong happened')
      sys.exit()

    self.b = self.b.T

    return True

  #######################################################################
  def observe(self):
    self.o = -1
    if self.auto_observations:
      rand = numpy.random.random_sample()
      acc = 0.0
      for i in range(len(self.observations)):
        acc += self.obs_mat[self.a, self.s, i]
        if acc > rand:
          self.o = i
          break
      if self.o == -1:
        print('Error: observation is not properly sampled')
        sys.exit()
    else:
      if self.s <= 11:
        item = 'SANDWICH'
      elif self.s > 11:
        item = 'COFFEE'
      else:
        exit('ITEM UNKNOWN')

      if int(self.s % 12 / 4) is 0:
        person = 'ALICE'
      elif int(self.s % 12 / 4) is 1:
        person = 'BOB'
      elif int(self.s % 12 / 4) is 2:
        person = 'CAROL'
      else:
        exit('PERSON UNKNOWN')

      if int(self.s % 4) is 0:
        room = 'OFFICE ONE'
      elif int(self.s % 4) is 1:
        room = 'OFFICE TWO'
      elif int(self.s % 4) is 2:
        room = 'LAB'
      elif int(self.s % 4) is 3:
        room = 'CONFERENCE ROOM'
      else:
        exit('ROOM UNKNOWN')

      print([item, person, room])
      time.sleep(1)
      
      tmp_a = int(self.a)
      if tmp_a is 0:
        subprocess.Popen('espeak "what item should I buy?"', shell=True)
      elif tmp_a is 1:
        subprocess.Popen('espeak "who is this delivery for?"', shell=True)
      elif tmp_a is 2:
        subprocess.Popen('espeak "which room should I deliver to?"', shell=True)
      elif tmp_a is 3:
        subprocess.Popen('espeak "should I buy sandwich?"', shell=True)
      elif tmp_a is 4:
        subprocess.Popen('espeak "should I buy coffee?"', shell=True)
      elif tmp_a is 5:
        subprocess.Popen('espeak "is this delivery for alice?"', shell=True)
      elif tmp_a is 6:
        subprocess.Popen('espeak "is this delivery for bob?"', shell=True)
      elif tmp_a is 7:
        subprocess.Popen('espeak "is this delivery for carol?"', shell=True)
      elif tmp_a is 8:
        subprocess.Popen('espeak "should i deliver it to office one?"', shell=True)
      elif tmp_a is 9:
        subprocess.Popen('espeak "should i deliver it to office two?"', shell=True)
      elif tmp_a is 10:
        subprocess.Popen('espeak "should i deliver it to the lab?"', shell=True)
      elif tmp_a is 11:
        subprocess.Popen('espeak "should i deliver it to the conference room?"', shell=True)

      recognizer = speech_recognizer.Recognizer(action=self.a)
      self.o = recognizer.recognize()

      print([item, person, room])
      if tmp_a is 0 and 0 <= self.o <= 1:  # item
        pass
      elif tmp_a is 0:
        self.o = random.randint(0, 2)
      elif tmp_a is 1 and 2 <= self.o <= 4:  # person
        pass
      elif tmp_a is 1:
        self.o = random.randint(2, 5)
      elif tmp_a is 2 and 5 <= self.o <= 8:  # room
        pass
      elif tmp_a is 2:
        self.o = random.randint(5, 9)
      elif 3 <= tmp_a <= 11 and 9 <= self.o <= 10:  # yes no
        pass
      elif 3 <= tmp_a <= 11:
        self.o = random.randint(9, 11)
      else:
        print('A trial has finished')
        sys.exit()

  #######################################################################
  def update(self):

    new_b = numpy.dot(self.b.T, self.trans_mat[self.a, :])

    new_b[0] = [new_b[0, i] * self.obs_mat[self.a, i, self.o] for i in
                range(len(self.states))]

    self.b = (new_b / sum(new_b.T)).T

    # print('belief: ')
    # print(self.b.T)
    return True

  #######################################################################
  def run(self):
    cost = 0
    self.r = 0.0
    self.init_belief()

    assert self.policy_switch is 'pomdp'
    cnt=0

    while True:
      if self.print_flag is True:
        print('\nstate: ' + self.states[self.s] + ' ' + str(self.s[0]))
        print('belief: ' + str(self.b.T))
        time.sleep(0.5)
      
      # if abs(cost) >= self.max_cost:
      #   self.a = self.policy_term.select_action(self.b)
      # elif abs(cost) < self.min_cost:
      #   self.a = self.policy_ask.select_action(self.b)
      # else:
      #   self.a = self.policy_full.select_action(self.b)

      self.a = self.policy_full.select_action(self.b)

      ################## TEMP #########
      # if cnt == 0:
      #   self.a = 4
      #   cnt += 1

      if self.print_flag is True:
        print('cost: ' + str(cost))
        print('action: ' + self.actions[int(self.a)] + ' ' + str(int(self.a)))


      self.observe()
      if self.print_flag is True:
        print('observation: ' + self.observations[self.o] + ' ' + str(self.o))
        print

      self.update()

      self.r += self.reward_mat[self.a, self.s]

      if 'take' not in self.actions[int(self.a)]:
        cost += self.reward_mat[self.a, self.s]
      else:
        break
    
    if self.print_flag is True:
      print('---------------------------------->')
      print('reward: ' + str(self.r))
      print('---------------------------------->')

    return cost

  #######################################################################
  def run_numbers_of_trials(self):

    cost_list = []
    success_list = []
    reward_list = []
    
    bar = Bar('Processing', max=self.trials_num)
    for i in range(self.trials_num):

      xk = numpy.arange(len(self.states))
      print(xk)
      print(self.pk)
      custm = stats.rv_discrete(name='custm', values=(xk, self.pk))
      self.s = custm.rvs(size=1)

      cost_list.append(self.run())
      reward_list.append(self.r)

      if int(self.a - (3 + self.num_item + self.num_person + self.num_room)) \
          == int(self.s):
        success_list.append(1)
      else:
        success_list.append(0)

      bar.next()

    bar.finish()

    cost_arr = numpy.array(cost_list)
    success_arr = numpy.array(success_list)
    reward_arr = numpy.array(reward_list)

    print('average cost: ' + str(numpy.mean(cost_arr))[1:] + ' with std ' + 
          str(numpy.std(cost_arr)))
    print('average success: ' + str(numpy.mean(success_arr)) + ' with std ' +
          str(numpy.std(success_arr)))
    print('average reward: ' + str(numpy.mean(reward_arr)) + ' with std ' + 
          str(numpy.std(reward_arr)))

    return (numpy.mean(cost_arr),numpy.mean(success_arr),numpy.mean(reward_arr))

def main():

  s = Simulator(uniform_init_belief=True, 
                policy_file_full='policy/20150411.policy', 
                pomdp_file='models/20150411.pomdp',
                print_flag=True, 
                actual_time='day', 
                robot_time='day', 
                policy_switch='pomdp',
                trials_num=10,
                min_cost=0,
                max_cost=1000,
                auto_observations=True,
                rounds=1,
                num_item=3,
                num_person=4,
                num_room=3)

  s.run_numbers_of_trials()


if __name__ == '__main__':

  main()

