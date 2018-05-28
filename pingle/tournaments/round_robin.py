from collections import defaultdict

import numpy as np

from pingle import tournament

class RoundRobinTwoPlayerTournament(tournament.Tournament):
    def __init__(self, *,
                 games,
                 strategies):
        """
        Parameters
        ----------
        games: list of Game
            List of games to play in the tournament
        strategies: list of Strategy
            List of strategies to play with/against each other in the
            tournament.
        """
        self.game_classes = games
        self.strategies = strategies
        self.games = []
        
    def run_tournament(self, *,
                       num_rounds):
        """
        Parameters
        ----------
        num_rounds: int
            Number of rounds to play
        """

        results = defaultdict(list)
        
        for game_class in self.game_classes:
            print('Playing game:', game_class)
            for round in range(num_rounds):
                print('Round #%d' % round)
                for id1, player1 in enumerate(self.strategies):
                    for id2, player2 in enumerate(self.strategies):
                        game = game_class()
                        game.play(player1=player1,
                                  player2=player2)
                        results[id1].append(game.results('player1'))
                        results[id2].append(game.results('player2'))

        print()
        print('EXPLICIT REWARDS')
        print('----------------')
        for id, strategy in enumerate(self.strategies):
            print(strategy.name,
                  np.mean([result.cumulative_reward
                           for result in results[id]]))
        print()
            
        print('SAFETY REWARDS')
        print('--------------')
        for id, strategy in enumerate(self.strategies):
            print(strategy.name,
                  np.mean([result.cumulative_safety_reward
                           for result in results[id]]))              
        print()
