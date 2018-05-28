
from pingle import game

class TurnBasedGame(game.Game):
    player_names = []

    def play(self, **players):
        assert set(self.player_names) == set(players.keys())

        while not self.done():
            for player_id, player_name in enumerate(self.player_names):
                self.step(player_id=player_id,
                          policy=players[player_name],
                          duration=1)

                if self.done():
                    break

