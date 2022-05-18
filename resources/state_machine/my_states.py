'''
here are the rules of state transition
'''


'''import all of states body classes'''
from resources.state_machine.states.s00_initialization import InitializationBody
from resources.state_machine.states.s01_close_program import CloseProgramBody
from resources.state_machine.states.s02_test_state_1 import Test1StateBody
from resources.state_machine.states.s03_test_state_2 import Test2StateBody

class Initialization(InitializationBody):
    def on_event(self, event):
        if event == 'device_locked':
            self.action()
        else:
            self.status = "error"

        if self.status == "GO TO TEST1":
            return Test1State()
        else:
            info = ">>> Info: transition error in {} state".format(self)
            return CloseProgram(info)

class CloseProgram(CloseProgramBody):
    def on_event(self, event):
        self.action()

class Test1State(Test1StateBody):
    def on_event(self, event):
        if event == 'device_locked':
            self.action()
        else:
            self.status = "error"

        if self.status == "GO TO TEST1":
            return Test1State()
        elif self.status == "GO TO TEST2":
            return Test2State()
        else:
            info = ">>> Info: transition error in {} state".format(self)
            return CloseProgram(info)

class Test2State(Test2StateBody):
    def on_event(self, event):
        if event == 'device_locked':
            self.action()
        else:
            self.status = "error"

        if self.status == "GO TO TEST1":
            return Test1State()
        elif self.status == "GO TO TEST2":
            return Test2State()
        else:
            info = ">>> Info: transition error in {} state".format(self)
            return CloseProgram(info)
