from time import sleep

class Test1StateBody(object):

    def __init__(self,):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """
        self.counter = 0
        self.next_state = self.__class__.__name__

    def run_state(self):

        self.counter += 1
        print("Output: {}".format(self.counter))
        sleep(0.5)
        if self.counter >= 3:
            self.next_state = "Test2State"

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__



