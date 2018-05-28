import abc

import pingle.core

class Policy:
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_action(self, *,
                   observation,
                   previous_reward,
                   public_speech):
        """
        Parameters
        ----------
        observation: Observation
            Observation given to the agent.
        previous_reward: float
            Reward given to the agent for the previous policy.
        public_speech: SpeechAct
            Speech acts aligned with the current observation.
        """
        pass
