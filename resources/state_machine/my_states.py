'''
here are the rules of state transition
'''


'''import all of states body classes'''
from resources.state_machine.states.s00_initialization import InitializationBody
from resources.state_machine.states.s01_close_program import CloseProgramBody
from resources.state_machine.states.s02_test_state_1 import Test1StateBody
from resources.state_machine.states.s03_test_state_2 import Test2StateBody

class Initialization(InitializationBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.Initialization

        '''control_word'''
        if event == 'device_locked':
            '''run your functions in this state'''
            self.run_state()
        else:
            states_data.CloseProgram.info = ">>> Info: device unlocked in {} state".format(self)
            return states_data.CloseProgram

        '''transition conditions'''
        if self.next_state == "Test1State":
            return states_data.Test1State
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram

class CloseProgram(CloseProgramBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.CloseProgram
        '''run your functions in this state'''
        self.run_state()

class Test1State(Test1StateBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.Test1State

        '''control_word'''
        if event == 'device_locked':
            '''run your functions in this state'''
            self.run_state()
        else:
            states_data.CloseProgram.info = ">>> Info: device unlocked in {} state".format(self)
            return states_data.CloseProgram

        '''transition conditions'''
        if self.next_state == "Test1State":
            return states_data.Test1State
        elif self.next_state == "Test2State":
            '''clear data before transition'''
            states_data.Test1State = Test1State()
            return states_data.Test2State
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram

class Test2State(Test2StateBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.Test2State

        '''control_word'''
        if event == 'device_locked':
            '''run your functions in this state'''
            self.run_state()
        else:
            states_data.CloseProgram.info = ">>> Info: device unlocked in {} state".format(self)
            return states_data.CloseProgram

        '''transition conditions'''
        if self.next_state == "Test1State":
            '''clear data before transition'''
            states_data.Test2State = Test2State()
            return states_data.Test1State
        elif self.next_state == "Test2State":
            return states_data.Test2State
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram
