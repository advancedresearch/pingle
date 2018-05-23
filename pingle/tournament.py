

class RoundRobinTwoPlayerTournament:
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
        self.strategies
        self.games = []
        
    def run_tournament(self, *,
                       num_rounds):
        """
        Parameters
        ----------
        num_rounds: int
            Number of rounds to play
        """

        for game_class in self.game_classes:
            print('Playing game:', game_class)
            for round in range(num_rounds):
                print('Round #%d' % round)
                for player1 in strategies:
                    for player2 in strategies:
                        game = game_class()
                        results = game.play(player1=player1,
                                            player2=player2)
                        print(results)
