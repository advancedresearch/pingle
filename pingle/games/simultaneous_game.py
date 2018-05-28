from pingle.games.turn_based_game import TurnBasedGame
from pingle.results import GameResults

class SimultaneousOneRoundGame(TurnBasedGame):
    def __init__(self):
        self._done = False
        self._actions_taken = [None, None]
        self._rewards_received = [None, None]
        self._safety_rewards_received = [None, None]
        
    def step(self, *, player_id, policy, duration):
        # the case that some player still has to move
        if not self.done():
            # get action
            action = policy.get_action(observation=0,
                                       previous_reward=0.0,
                                       public_speech=[])

            # validate input
            assert action in ['cooperate', 'defect']
            assert 0 <= player_id <= len(self.player_names)
            assert duration == 1

            self._actions_taken[player_id] = action
            
            if None not in self._actions_taken:
                self._done = True

                self._rewards_received = (
                    self.payoff_matrix[
                        tuple(self._actions_taken)])

                self._safety_rewards_received = (
                    self.safety_payoff_matrix[
                        tuple(self._actions_taken)])

    def done(self):
        return self._done

    def results(self, player_name):
        player_id = self.player_names.index(player_name)
        return GameResults(
            cumulative_reward=
            self._rewards_received[player_id],
            cumulative_safety_reward=
            self._safety_rewards_received[player_id],
        )
            
