import numpy as np

from pingle.core.policy import Policy


class RandomPolicy:
    actions = []
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
        assert len(self.actions) > 0, \
            'Should use an inheriting class which overrides actions'

        return np.random.choice(self.actions)
    
