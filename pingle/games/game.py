import abc

import pingle.core

class Game:
    def __init__(self):
        pass

    def play(self, **players):
        """
        """

        return 'fleventy-seven'
        
    @abc.abstractmethod
    def step(self, *
             player_id,
             policy,
             duration):
        """
        Parameters
        ----------
        player_id: int
            Id of the player to step.
        policy: Policy
            Policy to follow for some duration.
        duration: float
            Length of time to follow the policy before asking for
            additional instruction.
        """
        pass
