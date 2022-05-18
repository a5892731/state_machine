'''Sources:

https://gist.github.com/Karn/8fac5d8cc31a9a6b1e2bfb31e2a4267b
'''


'''import all your states here'''
from resources.state_machine.my_states import Initialization


class StateLoader(object): #in Karen project is a SimpleDevice class
    """
    A simple state machine that mimics the functionality of a device from a
    high level.
    """

    def __init__(self):
        """ Initialize the components. """

        # Start with a default state.
        self.state = Initialization()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """
        # The next state will be the result of the on_event function.

        self.state = self.state.on_event(event)



if __name__ == "__main__":
    device = StateLoader()

    while True:
        device.on_event("device_locked")