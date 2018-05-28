

class ConditionalSpeechAct:
    """Speech act which takes different values depending on who the
    speaker ends up being.
    """
    def __init__(self, **messages_by_player):
        self.player_names = messages.keys()
        self.messages = messages

class SpeechActTable:
    def __init__(self, **speech_acts_by_player):
        self.player_names = speech_acts_by_player.keys()
        self.speech_acts_by_player = speech_acts_by_player

class SpeechActMatrix:
    def __init__(self, **speech_acts_by_action):
        self.speech_acts_by_action = speech_acts_by_action

