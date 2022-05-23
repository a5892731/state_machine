'''
version 2.0
author: a5892731
date: 2021-03-17
update: 2022-05-23

description:
this is a simple state machine

sources:
https://karn-s.tumblr.com/post/163553561848/python-state-machine

required modules:


'''
from time import time

from resources.state_machine.state_loader import StateLoader

#--------------------------------------------------------------------------------------- <<<< MAIN LOOP



if __name__ == "__main__":
    device = StateLoader()
    while True:
        start_time = time()


        device.on_event('device_locked') # call the state machine events


        loop_time = time() - start_time
        print(">>> main loop time = {}".format(loop_time))