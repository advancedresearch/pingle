

from pingle.games.game import Game
from pingle.policies.constant import ConstantPolicy

class SimplePrisonersDilemma(Game):
    def __init__(self):
        self.actions = {0: None, 1: None}

    def _done(self):
        return not (None in self.actions.values())
        
    def step(self, *, player_id, policy, duration):
        # the case that some player still has to move
        if not self._done():
            # get action
            action = policy.get_action(observation=0,
                                       previous_reward=0.0,
                                       public_speech=[])

            # normalize action
            action = self.normalize_action(action)

            # validate input
            assert action in ['cooperate', 'defect']
            assert player_id in [0, 1]
            assert duration >= 0.0

            self.actions[player_id] = action

        else:
            pass

    def observe(self):
        if 


class CooperatePolicy(ConstantPolicy):
    action = 'cooperate'
    
class DefectPolicy(ConstantPolicy):
    action = 'defect'

