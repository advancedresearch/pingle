from pingle.core.persona import Persona

class TabularPersona(Persona):
    speech_act_table = None
    
    def __init__(self, player_name, game):
        self.player_name = player_name
        self.game = game

    def speak(self):
        """Need to fill this in!"""
        raise NotImplementedError

