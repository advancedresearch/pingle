import abc

class Tournament:
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
        pass

    @abc.abstractmethod
    def run_tournament(self, *,
                       num_rounds):
        """
        Parameters
        ----------
        num_rounds: int
            Number of rounds to play
        """

        pass
