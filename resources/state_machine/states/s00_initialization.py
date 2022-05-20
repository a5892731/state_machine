class InitializationBody(object):
    def __init__(self,):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """

        self.status = None

    def action(self):
        print(self)
        self.status = "GO TO TEST1"


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


