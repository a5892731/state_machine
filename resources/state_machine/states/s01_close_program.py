

class CloseProgramBody(object):

    def __init__(self, info):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """
        self.info = info

    def action(self):
        print(self)
        print(self.info)
        quit()

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


