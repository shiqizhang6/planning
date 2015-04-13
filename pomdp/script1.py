#!/usr/bin/env python

from simulator import Simulator

# ######################################
# s = Simulator(
#               uniform_init_belief=True, 
#               policy_file_full='policy/cost5.policy', 
#               print_flag=False, 
#               actual_time='morning', 
#               robot_time='morning', 
#               policy_switch='pomdp',
#               trials_num=10000,
#               min_cost=0,
#               max_cost=1000,
#               auto_observations=True,
#               rounds=1
#              )
# c0, s0, r0 = s.run_numbers_of_trials()
# print('average cost: ' + str(c0))
# print('average success: ' + str(s0))
# print('average reward: ' + str(r0))
# 
# ######################################
# s = Simulator(
#               uniform_init_belief=True, 
#               policy_file_full='policy/cost5.policy', 
#               print_flag=False, 
#               actual_time='noon', 
#               robot_time='noon', 
#               policy_switch='pomdp',
#               trials_num=10000,
#               min_cost=0,
#               max_cost=1000,
#               auto_observations=True,
#               rounds=1
#              )
# c1, s1, r1 = s.run_numbers_of_trials()
# print('average cost: ' + str(c1))
# print('average success: ' + str(s1))
# print('average reward: ' + str(r1))
# 
# ######################################
# s = Simulator(
#               uniform_init_belief=True, 
#               policy_file_full='policy/cost5.policy', 
#               print_flag=False, 
#               actual_time='afternoon', 
#               robot_time='afternoon', 
#               policy_switch='pomdp',
#               trials_num=10000,
#               min_cost=0,
#               max_cost=1000,
#               auto_observations=True,
#               rounds=1
#              )
# c2, s2, r2 = s.run_numbers_of_trials()
# print('average cost: ' + str(c2))
# print('average success: ' + str(s2))
# print('average reward: ' + str(r2))
# 
# ######################################
# ######################################
# print
# print('average cost: ' + str((c0+c1+c2)/3.0))
# print('average success: ' + str((s0+s1+s2)/3.0))
# print('average reward: ' + str((r0+r1+r2)/3.0))
# print

######################################
######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost10.policy', 
              print_flag=False, 
              actual_time='morning', 
              robot_time='morning', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c0, s0, r0 = s.run_numbers_of_trials()
print('average cost: ' + str(c0))
print('average success: ' + str(s0))
print('average reward: ' + str(r0))

######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost10.policy', 
              print_flag=False, 
              actual_time='noon', 
              robot_time='noon', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c1, s1, r1 = s.run_numbers_of_trials()
print('average cost: ' + str(c1))
print('average success: ' + str(s1))
print('average reward: ' + str(r1))

######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost10.policy', 
              print_flag=False, 
              actual_time='afternoon', 
              robot_time='afternoon', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c2, s2, r2 = s.run_numbers_of_trials()
print('average cost: ' + str(c2))
print('average success: ' + str(s2))
print('average reward: ' + str(r2))

######################################
######################################
print
print('average cost: ' + str((c0+c1+c2)/3.0))
print('average success: ' + str((s0+s1+s2)/3.0))
print('average reward: ' + str((r0+r1+r2)/3.0))
print

######################################
######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost20.policy', 
              print_flag=False, 
              actual_time='morning', 
              robot_time='morning', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c0, s0, r0 = s.run_numbers_of_trials()
print('average cost: ' + str(c0))
print('average success: ' + str(s0))
print('average reward: ' + str(r0))

######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost20.policy', 
              print_flag=False, 
              actual_time='noon', 
              robot_time='noon', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c1, s1, r1 = s.run_numbers_of_trials()
print('average cost: ' + str(c1))
print('average success: ' + str(s1))
print('average reward: ' + str(r1))

######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost20.policy', 
              print_flag=False, 
              actual_time='afternoon', 
              robot_time='afternoon', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c2, s2, r2 = s.run_numbers_of_trials()
print('average cost: ' + str(c2))
print('average success: ' + str(s2))
print('average reward: ' + str(r2))

######################################
######################################
print
print('average cost: ' + str((c0+c1+c2)/3.0))
print('average success: ' + str((s0+s1+s2)/3.0))
print('average reward: ' + str((r0+r1+r2)/3.0))
print

######################################
######################################
######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost40.policy', 
              print_flag=False, 
              actual_time='morning', 
              robot_time='morning', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c0, s0, r0 = s.run_numbers_of_trials()
print('average cost: ' + str(c0))
print('average success: ' + str(s0))
print('average reward: ' + str(r0))

######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost40.policy', 
              print_flag=False, 
              actual_time='noon', 
              robot_time='noon', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c1, s1, r1 = s.run_numbers_of_trials()
print('average cost: ' + str(c1))
print('average success: ' + str(s1))
print('average reward: ' + str(r1))

######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost40.policy', 
              print_flag=False, 
              actual_time='afternoon', 
              robot_time='afternoon', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c2, s2, r2 = s.run_numbers_of_trials()
print('average cost: ' + str(c2))
print('average success: ' + str(s2))
print('average reward: ' + str(r2))

######################################
######################################
print
print('average cost: ' + str((c0+c1+c2)/3.0))
print('average success: ' + str((s0+s1+s2)/3.0))
print('average reward: ' + str((r0+r1+r2)/3.0))
print
######################################
######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost60.policy', 
              print_flag=False, 
              actual_time='morning', 
              robot_time='morning', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c0, s0, r0 = s.run_numbers_of_trials()
print('average cost: ' + str(c0))
print('average success: ' + str(s0))
print('average reward: ' + str(r0))

######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost60.policy', 
              print_flag=False, 
              actual_time='noon', 
              robot_time='noon', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c1, s1, r1 = s.run_numbers_of_trials()
print('average cost: ' + str(c1))
print('average success: ' + str(s1))
print('average reward: ' + str(r1))

######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost60.policy', 
              print_flag=False, 
              actual_time='afternoon', 
              robot_time='afternoon', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c2, s2, r2 = s.run_numbers_of_trials()
print('average cost: ' + str(c2))
print('average success: ' + str(s2))
print('average reward: ' + str(r2))

######################################
######################################
print
print('average cost: ' + str((c0+c1+c2)/3.0))
print('average success: ' + str((s0+s1+s2)/3.0))
print('average reward: ' + str((r0+r1+r2)/3.0))
print
######################################
######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost80.policy', 
              print_flag=False, 
              actual_time='morning', 
              robot_time='morning', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c0, s0, r0 = s.run_numbers_of_trials()
print('average cost: ' + str(c0))
print('average success: ' + str(s0))
print('average reward: ' + str(r0))

######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost80.policy', 
              print_flag=False, 
              actual_time='noon', 
              robot_time='noon', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c1, s1, r1 = s.run_numbers_of_trials()
print('average cost: ' + str(c1))
print('average success: ' + str(s1))
print('average reward: ' + str(r1))

######################################
s = Simulator(
              uniform_init_belief=True, 
              policy_file_full='policy/cost80.policy', 
              print_flag=False, 
              actual_time='afternoon', 
              robot_time='afternoon', 
              policy_switch='pomdp',
              trials_num=10000,
              min_cost=0,
              max_cost=1000,
              auto_observations=True,
              rounds=1
             )
c2, s2, r2 = s.run_numbers_of_trials()
print('average cost: ' + str(c2))
print('average success: ' + str(s2))
print('average reward: ' + str(r2))

######################################
######################################
print
print('average cost: ' + str((c0+c1+c2)/3.0))
print('average success: ' + str((s0+s1+s2)/3.0))
print('average reward: ' + str((r0+r1+r2)/3.0))
print

