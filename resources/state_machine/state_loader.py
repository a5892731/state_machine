'''Sources:

https://gist.github.com/Karn/8fac5d8cc31a9a6b1e2bfb31e2a4267b
'''


'''import all your states here'''
from resources.state_machine.my_states import Initialization, CloseProgram, Test1State, Test2State

class States():
    def __init__(self):
        '''information variables'''
        self.current_state = None
        '''init all your states here
        this class stores memory of States'''
        self.Initialization = Initialization()
        self.CloseProgram = CloseProgram()
        self.Test1State = Test1State()
        self.Test2State = Test2State()


class StateLoader(object): #in Karen project this is a SimpleDevice class
    """
    A simple state machine that mimics the functionality of a device from a
    high level.
    """

    def __init__(self):
        """ Initialize the components. """
        # Initialize all states for memory storage purposes
        self.states_data = States()
        # Select an initial state
        self.state = self.states_data.Initialization

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """
        # Save down the name of the currently called state
        self.states_data.current_state = self.state.__class__.__name__
        print(">>> currently called state: {}".format(self.states_data.current_state)) # only for testing purposes

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event=event, states_data=self.states_data)



if __name__ == "__main__":
    device = StateLoader()

    while True:
        device.on_event("device_locked")