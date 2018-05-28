import abc

class Persona:
    def __init__(self, player_name, game):
        self.player_name = player_name
        self.game = game

    @abc.abstractmethod
    def speak(self):
        pass

