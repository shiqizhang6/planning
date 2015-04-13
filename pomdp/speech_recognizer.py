#!/usr/bin/env python

import subprocess
import sys
import os
import signal
import time

class Recognizer(object):

  def __init__(self, 
               executable_path='/home/szhang/software/cmu_sphinx/install/pocketsphinx/bin/pocketsphinx_continuous',
               item_path='/home/szhang/docs/Publications/conferences/2015_aaai_dialog/code/pomdp/config/speech/items',
               person_path='/home/szhang/docs/Publications/conferences/2015_aaai_dialog/code/pomdp/config/speech/persons',
               room_path='/home/szhang/docs/Publications/conferences/2015_aaai_dialog/code/pomdp/config/speech/rooms',
               yes_no_path='/home/szhang/docs/Publications/conferences/2015_aaai_dialog/code/pomdp/config/speech/yes_no',
               action = -1
              ):
    
    self.executable_path = executable_path
    self.item_path = item_path
    self.person_path = person_path
    self.room_path = room_path
    self.yes_no_path = yes_no_path

    self.action = action

  #####################################################################
  def recognize(self):

    if int(self.action) is 0:
      # here sphinx continuous
      p = subprocess.Popen(self.executable_path + \
          ' -dict ' + self.item_path + '/words.dic ' +\
          ' -lm ' + self.item_path + '/words.lm', \
          shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

      while p.poll() is None:
        l = p.stdout.readline() # This blocks until a newline
        if '000000000:' in l:
          output = l[11:]
          print('You said: ' + output)

          os.killpg(p.pid, signal.SIGTERM)
          if 'SANDWICH' in output:
            return 0
          elif 'COFFEE' in output:
            return 1
          else:
            subprocess.Popen('espeak "You said a word I do not understand"', \
                shell=True)
            time.sleep(5)
            return -1

    elif int(self.action) is 1:
      p = subprocess.Popen(self.executable_path + \
          ' -dict ' + self.person_path + '/words.dic ' +\
          ' -lm ' + self.person_path + '/words.lm', \
          shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

      while p.poll() is None:
        l = p.stdout.readline() # This blocks until a newline
        if '000000000:' in l:
          output = l[11:]
          print('You said: ' + output)

          os.killpg(p.pid, signal.SIGTERM)
          if 'ALICE' in output:
            return 2
          elif 'BOB' in output:
            return 3
          elif 'CAROL' in output:
            return 4
          else:
            subprocess.Popen('espeak "You said a word I do not understand"', \
                shell=True)
            time.sleep(5)
            return -1

    elif int(self.action) is 2:
      p = subprocess.Popen(self.executable_path + \
          ' -dict ' + self.room_path + '/words.dic ' +\
          ' -lm ' + self.room_path + '/words.lm', \
          shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

      while p.poll() is None:
        l = p.stdout.readline() # This blocks until a newline
        if '000000000:' in l:
          output = l[11:]
          print('You said: ' + output)

          os.killpg(p.pid, signal.SIGTERM)
          if 'OFFICE ONE' in output:
            return 5
          elif 'OFFICE TWO' in output:
            return 6
          elif 'LAB' in output:
            return 7
          elif 'CONFERENCE' in output:
            return 8
          else:
            subprocess.Popen('espeak "You said a word I do not understand"', \
                shell=True)
            time.sleep(5)
            return -1

    elif 3 <= int(self.action) <= 11:
      p = subprocess.Popen(self.executable_path + \
          ' -dict ' + self.yes_no_path + '/words.dic ' +\
          ' -lm ' + self.yes_no_path + '/words.lm', \
          shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

      while p.poll() is None:
        l = p.stdout.readline() # This blocks until a newline
        if '000000000:' in l:
          output = l[11:]
          print('You said: ' + output)

          os.killpg(p.pid, signal.SIGTERM)

          if 'YES' in output:
            return 9
          elif 'NO' in output:
            return 10
          else:
            subprocess.Popen('espeak "You said a word I do not understand"', \
                shell=True)
            time.sleep(5)
            return -1
    elif int(self.action) > 11:
      subprocess.Popen('espeak "thanks"', shell=True)
      print('SHOPPING REQUEST RECOGNIZED:')
    else:
      print('Something wrong in speech recognition module: self.action=', \
          str(self.action))
      sys.exit()



def main():
  r = Recognizer(action=3)
  r.recognize()

if __name__ == '__main__':
  main()


