from pingle.core.policy import Policy

class ConstantPolicy(Policy):
    action = None
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
        assert self.action is not None, \
            'Should use an inheriting class which overrides action'

        return self.action
    
