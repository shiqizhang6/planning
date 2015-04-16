#!/usr/bin/env python

import numpy as np
import time

class State(object):

    def __init__(self, item, person, room, num_item, num_person, num_room):
        
        self.item = item
        self.person = person
        self.room = room
        self.num_item = num_item
        self.num_person = num_person
        self.num_room = num_room

        self.index = (item * num_person * num_room) + (person * num_room) + room

    def getItemIndex(self):
        return self.item

    def getPersonIndex(self):
        return self.person

    def getRoomIndex(self):
        return self.room

    def getName(self):
        return 'i' + str(self.item) + '_p' + str(self.person) + '_r' + \
            str(self.room)

    def getIndex(self):
        return self.index

class Action(object):

    # qd_type: type of this action: ask or deliver? 
    def __init__(self, qd_type):
        
        assert qd_type in ['ask', 'deliver']
        self.qd_type = qd_type

class ActionAsk(Action):

    def __init__(self, q_type):

        assert q_type in ['wh', 'polar']
        Action.__init__(self, 'ask')
        self.q_type = q_type

class ActionAskWh(ActionAsk):

    def __init__(self, var):

        assert var in ['item', 'person', 'room']
        ActionAsk.__init__(self, 'wh')
        self.var = var

    def getName(self):
        if self.var == 'item':
            return 'ask_i'
        elif self.var == 'person':
            return 'ask_p'
        elif self.var == 'room':
            return 'ask_r'

    def getIndex(self):
        
        if self.var == 'item':
            return 0
        elif self.var == 'person':
            return 1
        elif self.var == 'room':
            return 2


class ActionAskPolar(ActionAsk):

    def __init__(self, var, num_item, num_person, num_room):

        ActionAsk.__init__(self, 'polar')
        self.num_item = num_item
        self.num_person = num_person
        self.num_room = num_room
        assert var in ['item', 'person', 'room']
        self.var = var

class ActionAskPolarItem(ActionAskPolar):

    def __init__(self, item, num_item, num_person, num_room):

        assert item < num_item
        ActionAskPolar.__init__(self, 'item', num_item, num_person, num_room)
        self.item = item

    def getItemIndex(self):
        return self.item

    def getIndex(self):
        return 3 + self.item

    def getName(self):
        return 'confirm_i' + str(self.item)

class ActionAskPolarPerson(ActionAskPolar):

    def __init__(self, person, num_item, num_person, num_room):
        
        assert person < num_person
        ActionAskPolar.__init__(self, 'person', num_item, num_person, num_room)
        self.person = person

    def getPersonIndex(self):
        return self.person

    def getIndex(self):
        return 3 + self.num_item + self.person

    def getName(self):
        return 'confirm_p' + str(self.person)

class ActionAskPolarRoom(ActionAskPolar):

    def __init__(self, room, num_item, num_person, num_room):
        
        assert room < num_room
        ActionAskPolar.__init__(self, 'room', num_item, num_person, num_room)
        self.room = room

    def getRoomIndex(self):
        return self.room

    def getIndex(self):
        return 3 + self.num_item + self.num_person + self.room

    def getName(self):
        return 'confirm_r' + str(self.room)

class ActionDeliver(Action):

    def __init__(self, item, person, room, num_item, num_person, num_room):

        assert item < num_item
        assert person < num_person
        assert room < num_room
        Action.__init__(self, 'deliver')
        self.item = item
        self.person = person
        self.room = room
        self.num_item = num_item
        self.num_person = num_person
        self.num_room = num_room

    def getItemIndex(self):
        return self.item

    def getPersonIndex(self):
        return self.person

    def getRoomIndex(self):
        return self.room

    def getIndex(self):
        return 3 + self.num_item + self.num_person + self.num_room + \
            (self.item * self.num_person * self.num_room) + \
            (self.person * self.num_room) + self.room

    def getName(self):
        return 'take_i' + str(self.item) + '_p' + str(self.person) + '_r' + \
            str(self.room)

class Observation(object):

    def __init__(self, qd_type):
    
        assert qd_type in ['wh', 'polar']
        self.qd_type = qd_type

class ObservationWh(Observation):

    def __init__(self, var):

        assert var in ['item', 'person', 'room']
        Observation.__init__(self, 'wh')
        self.var = var

class ObservationWhItem(ObservationWh):

    def __init__(self, item, num_item, num_person, num_room):

        assert item < num_item
        ObservationWh.__init__(self, 'item')
        self.item = item
        self.num_item = num_item
        self.num_person = num_person
        self.num_room = num_room

    def getItemIndex(self):
        return self.item

    def getIndex(self):
        return self.item

    def getName(self):
        return 'i' + str(self.item)


class ObservationWhPerson(ObservationWh):

    def __init__(self, person, num_item, num_person, num_room):

        assert person < num_person
        ObservationWh.__init__(self, 'person')
        self.person = person
        self.num_item = num_item
        self.num_person = num_person
        self.num_room = num_room

    def getPersonIndex(self):
        return self.person

    def getIndex(self):
        return self.num_item + self.person

    def getName(self):
        return 'p' + str(self.person)

class ObservationWhRoom(ObservationWh):

    def __init__(self, room, num_item, num_person, num_room):

        assert room < num_room
        ObservationWh.__init__(self, 'room')
        self.room = room
        self.num_item = num_item
        self.num_person = num_person
        self.num_room = num_room

    def getRoomIndex(self):
        return self.room

    def getIndex(self):
        return self.num_item + self.num_person + self.room

    def getName(self):
        return 'r' + str(self.room)

class ObservationPolar(Observation):

    def __init__(self, polar, num_item, num_person, num_room):

        assert polar in ['yes', 'no']
        Observation.__init__(self, 'polar')
        self.polar = polar
        self.num_item = num_item
        self.num_person = num_person
        self.num_room = num_room

    def getName(self):
        if self.polar == 'yes':
            return 'yes'
        elif self.polar == 'no':
            return 'no'

    def getIndex(self):
        if self.polar == 'yes':
            return self.num_item + self.num_person + self.num_room
        elif self.polar == 'no':
            return self.num_item + self.num_person + self.num_room + 1

class PomdpGenerator(object):

    def __init__(self, num_item, num_person, num_room, r_max, r_min, \
        weight_i, weight_p, weight_r):
        
        self.filename = 'models/' + time.strftime('%Y%m%d') + '.pomdp'
        self.num_item = num_item
        self.num_person = num_person
        self.num_room = num_room

        self.r_max = r_max
        self.r_min = r_min

        self.weight_i = weight_i
        self.weight_p = weight_p
        self.weight_r = weight_r

        self.magic_number = 0.1
        self.polar_tp_rate = 0.95
        self.polar_tn_rate = 0.95

        self.state_set = []
        self.action_set = []
        self.observation_set = []

        self.trans_mat = None
        self.obs_mat = None
        self.reward_mat = None


        # compute the sets of states, actions, observations
        self.state_set = self.computeStateSet(self.num_item, self.num_person,
            self.num_room)
        self.action_set = self.computeActionSet(self.num_item, self.num_person,
            self.num_room)
        self.observation_set = self.computeObservationSet(self.num_item, 
            self.num_person, self.num_room)

        # compute the functions of transition, observation, reward
        self.trans_mat = self.computeTransFunction(self.num_item,
            self.num_person, self.num_room)
        self.obs_mat = self.computeObsFunction(self.num_item, self.num_person,
            self.num_room, self.magic_number, self.polar_tp_rate)
        self.reward_mat = self.computeRewardFunction(self.num_item,
            self.num_person, self.num_room, self.r_max, self.r_min, \
            self.weight_i, self.weight_p, self.weight_r)

        self.writeToFile()

    def computeTransFunction(self, num_item, num_person, num_room):

        # as this problem is specific, this can be manually done
        trans_mat = np.ones((len(self.action_set), len(self.state_set), 
            len(self.state_set)))

        for action in self.action_set:
            if action.qd_type == 'ask':
                trans_mat[action.getIndex()] = np.eye(len(self.state_set), 
                    dtype=float)
            elif action.qd_type == 'deliver':
                trans_mat[action.getIndex()] = np.ones((len(self.state_set),
                len(self.state_set))) / float(len(self.state_set))

        return trans_mat

    # HERE WE INTRODUCE A NOVEL OBSERVATION MODEL
    # true-positive rate = 1/(n^0.1), where n is the variable's range
    def computeObsFunction(self, num_item, num_person, num_room, magic_number,
        polar_tp_rate):
        
        obs_mat = np.zeros((len(self.action_set), len(self.state_set),
            len(self.observation_set)))

        for action in self.action_set:

            if action.qd_type == 'deliver':
                obs_mat[action.getIndex()] = np.ones((len(self.state_set), 
                    len(self.observation_set))) / len(self.observation_set)

            elif action.qd_type == 'ask':
                if action.q_type == 'wh':
                    if action.var == 'item':
                        tp_rate = 1.0 / pow(num_item, 0.1)
                        for state in self.state_set:
                            for observation in self.observation_set:
                                if observation.qd_type == 'wh':
                                    if observation.var == 'item':
                                        if observation.getItemIndex() == \
                                            state.getItemIndex():
                                            
                                            obs_mat[action.getIndex()]\
                                                [state.getIndex()]\
                                                [observation.getIndex()] = \
                                                tp_rate
                                        else:
                                            obs_mat[action.getIndex()]\
                                                [state.getIndex()]\
                                                [observation.getIndex()] = \
                                                (1.0-tp_rate) / (num_item-1)
                                    
                    elif action.var == 'person':
                        tp_rate = 1.0 / pow(num_person, 0.1)
                        for state in self.state_set:
                            for observation in self.observation_set:
                                if observation.qd_type == 'wh':
                                    if observation.var == 'person':
                                        if observation.getPersonIndex() == \
                                            state.getPersonIndex():
                                            
                                            obs_mat[action.getIndex()]\
                                                [state.getIndex()]\
                                                [observation.getIndex()]\
                                                = tp_rate
                                        else:
                                            obs_mat[action.getIndex()]\
                                                [state.getIndex()]\
                                                [observation.getIndex()]\
                                                = (1.0-tp_rate) / (num_person-1)

                    elif action.var == 'room':
                        tp_rate = 1.0 / pow(num_room, 0.1)
                        for state in self.state_set:
                            for observation in self.observation_set:
                                if observation.qd_type == 'wh':
                                    if observation.var == 'room':
                                        if observation.getRoomIndex() ==\
                                            state.getRoomIndex():
                                            
                                            obs_mat[action.getIndex()]\
                                                [state.getIndex()]\
                                                [observation.getIndex()]\
                                                = tp_rate
                                        else:
                                            obs_mat[action.getIndex()]\
                                                [state.getIndex()]\
                                                [observation.getIndex()]\
                                                = (1.0-tp_rate) / (num_room-1)
                    
                elif action.q_type == 'polar':
                    if action.var == 'item':
                        for state in self.state_set:
                            for observation in self.observation_set:
                                if observation.getName() == 'yes':
                                    if state.getItemIndex() ==\
                                        action.getItemIndex():
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()]\
                                            = self.polar_tp_rate
                                    else:
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()] = \
                                            1.0 - self.polar_tp_rate
                                elif observation.getName() == 'no':
                                    if state.getItemIndex() ==\
                                        action.getItemIndex():
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()]= \
                                            1.0 - self.polar_tn_rate
                                    else:
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()] \
                                            = self.polar_tn_rate
                    elif action.var == 'person':
                        for state in self.state_set:
                            for observation in self.observation_set:
                                if observation.getName() == 'yes':
                                    if state.getPersonIndex() == \
                                        action.getPersonIndex():
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()]\
                                            = self.polar_tp_rate
                                    else:
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()]=\
                                            1.0 - self.polar_tp_rate
                                elif observation.getName() == 'no':
                                    if state.getPersonIndex() == \
                                        action.getPersonIndex():
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()]= \
                                            1.0 - self.polar_tn_rate
                                    else:
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()]=\
                                            self.polar_tn_rate
                    elif action.var == 'room':
                        for state in self.state_set:
                            for observation in self.observation_set:
                                if observation.getName() == 'yes':
                                    if state.getRoomIndex() ==\
                                        action.getRoomIndex():
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()]\
                                            = self.polar_tp_rate
                                    else:
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()]=\
                                            1.0 - self.polar_tp_rate
                                elif observation.getName() == 'no':
                                    if state.getRoomIndex() ==\
                                        action.getRoomIndex():
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()]= \
                                            1.0 - self.polar_tn_rate
                                    else:
                                        obs_mat[action.getIndex()]\
                                            [state.getIndex()]\
                                            [observation.getIndex()]\
                                            = self.polar_tn_rate

        return obs_mat

    def computeRewardFunction(self, num_item, num_person, num_room,
        r_max, r_min, weight_i, weight_p, weight_r):

        reward_mat = np.zeros((len(self.action_set), len(self.state_set), ))

        for action in self.action_set:

            if action.qd_type == 'ask':

                if action.q_type == 'wh':
                    reward_mat[action.getIndex()] = -1
                elif action.q_type == 'polar':
                    reward_mat[action.getIndex()] = -2

            elif action.qd_type == 'deliver':
                
                for state in self.state_set:

                    reward_mat[action.getIndex()][state.getIndex()] = \
                        (r_max - r_min) * \
                        weight_i[action.getItemIndex()][state.getItemIndex()]*\
                        weight_p[action.getPersonIndex()][state.getPersonIndex()]*\
                        weight_r[action.getRoomIndex()][state.getRoomIndex()]\
                        + r_min

        return reward_mat

    def computeStateSet(self, num_item, num_person, num_room):

        ret = []
        for i in range(num_item):
            for p in range(num_person):
                for r in range(num_room):
                    ret.append(State(i, p, r, num_item, num_person, num_room))

        return ret

    def computeActionSet(self, num_item, num_person, num_room):

        ret = []
        ret.append(ActionAskWh('item'))
        ret.append(ActionAskWh('person'))
        ret.append(ActionAskWh('room'))
        
        for i in range(num_item):
            ret.append(ActionAskPolarItem(i, num_item, num_person, num_room))

        for p in range(num_person):
            ret.append(ActionAskPolarPerson(p, num_item, num_person, num_room))

        for r in range(num_room):
            ret.append(ActionAskPolarRoom(r, num_item, num_person, num_room))

        for i in range(num_item):
            for p in range(num_person):
                for r in range(num_room):
                    ret.append(ActionDeliver(i, p, r, num_item, num_person,
                        num_room))

        return ret

    def computeObservationSet(self, num_item, num_person, num_room):

        ret = []
        for i in range(num_item):
            ret.append(ObservationWhItem(i, num_item, num_person, num_room))

        for p in range(num_person):
            ret.append(ObservationWhPerson(p, num_item, num_person, num_room))

        for r in range(num_room):
            ret.append(ObservationWhRoom(r, num_item, num_person, num_room))

        ret.append(ObservationPolar('yes', num_item, num_person, num_room))
        ret.append(ObservationPolar('no', num_item, num_person, num_room))

        return ret

    def writeToFile(self):

        f = open(self.filename, 'w')

        # first few lines
        s = ''
        s += 'discount : 0.9\n\nvalues: reward\n\nstates: '

        # section of states
        for state in self.state_set:
            s += state.getName() + ' '

        # section of actions
        s += '\n\nactions: '

        for action in self.action_set:
            s += action.getName() + ' '

        # section of observations
        s += '\n\nobservations: '

        for observation in self.observation_set:
            s += observation.getName() + ' ' 

        # section of transition matrix
        for action in self.action_set:
            if action.qd_type == 'ask':
                s += '\n\nT: ' + action.getName() + '\nidentity'
            elif action.qd_type == 'deliver':
                s += '\n\nT: ' + action.getName() + '\nuniform'

        s += '\n'

        # section of observation matrix
        for action in self.action_set:
            s += '\nO: ' + action.getName() + '\n'
            for state in self.state_set:
                for observation in self.observation_set:
                    s += str(self.obs_mat[action.getIndex()]\
                        [state.getIndex()]\
                        [observation.getIndex()]) + ' '
                s += '\n'

        s += '\n'

        # sectoin of reward matrix
        for action in self.action_set:
            for state in self.state_set:
                s += 'R: ' + action.getName() + '\t\t: ' + state.getName() + \
                    '\t: *\t\t: * ' + \
                    str(self.reward_mat[action.getIndex()][state.getIndex()]) + '\n'

        f.write(s)
        f.close()

def main():

    num_item = 4
    num_person = 4
    num_room = 3

    r_max = 50.0
    r_min = -100.0

    old_reward = True

    weight_i = np.array([[1.0, 0.25, 0.25, 0.125], 
                         [0.25, 1.0, 0.5, 0.125], 
                         [0.25, 0.5, 1.0, 0.125], 
                         [0.125, 0.125, 0.125, 1.0]])

    weight_p = np.array([[1.0, 0.0, 0.0, 0.0], 
                         [0.0, 1.0, 0.5, 0.0], 
                         [0.0, 0.5, 1.0, 0.0], 
                         [0.0, 0.0, 0.0, 1.0]])

    weight_r = np.array([[1.0, 3.0/7.0, 2.0/7.0], 
                         [3.0/7.0, 1.0, 0.0], 
                         [2.0/7.0, 0.0, 1.0]])

    
    if old_reward:
        weight_i = weight_i.astype(int)
        weight_p = weight_p.astype(int)
        weight_r = weight_r.astype(int)

    pg = PomdpGenerator(num_item, num_person, num_room, r_max, r_min, \
        weight_i, weight_p, weight_r)

if __name__ == '__main__':

    main()



