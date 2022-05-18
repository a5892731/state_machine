'''
version 2.0
author: a5892731
date: 2021-03-17
update: 2022-05-18

description:
this is a simple state machine

sources:
https://karn-s.tumblr.com/post/163553561848/python-state-machine

required modules:


'''

from resources.state_machine.state_loader import StateLoader


#--------------------------------------------------------------------------------------- <<<< MAIN MENU



if __name__ == "__main__":
    device = StateLoader()

    while True:
        device.on_event('device_locked')