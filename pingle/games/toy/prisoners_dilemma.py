from pingle import registry_acts
from pingle.games.simultaneous_game import SimultaneousOneRoundGame
from pingle.policies.constant import ConstantPolicy
from pingle.policies.random import RandomPolicy
from pingle.core.speech_acts import (
    SpeechActTable, SpeechActMatrix, ConditionalSpeechAct)
from pingle.personas import TabularPersona

@registry.register_game('v0')
class SimplePrisonersDilemma(SimultaneousOneRoundGame):
    player_names = ['player1', 'player2']
    actions = ['cooperate', 'defect']

    payoff_matrix = {
        ('cooperate', 'cooperate'): (7, 7),
        ('cooperate', 'defect'): (0, 10),
        ('defect', 'cooperate'): (10, 0),
        ('defect', 'defect'): (3, 3),
    }

    safety_payoff_matrix = {
        ('cooperate', 'cooperate'): (1, 1),
        ('cooperate', 'defect'): (1, 0),
        ('defect', 'cooperate'): (0, 1),
        ('defect', 'defect'): (0, 0),
    }


class PrisonersDilemmaPersona(TabularPersona):
    """Base class for PD personas"""
    @property
    def speech_act_table(self):
        SpeechActTable(
            player1=SpeechActMatrix(
                cooperate=SpeechActTable(
                    player2=SpeechActMatrix(
                        cooperate=ConditionalSpeechAct(
                            player1=self.mutual_cooperation_strings,
                            player2=self.mutual_cooperation_strings
                            ),
                        defect=ConditionalSpeechAct(
                            player1=self.betrayee_strings,
                            player2=self.betrayer_strings))),
                defect=SpeechActTable(
                    player2=SpeechActMatrix(
                        cooperate=ConditionalSpeechAct(
                            player1=self.betrayer_strings,
                            player2=self.betrayee_strings
                            ),
                        defect=ConditionalSpeechAct(
                            player1=self.mutual_betrayal_strings,
                            player2=self.mutual_betrayal_strings)))))


@registry.register_persona(SimplePrisonersDilemma, 'v0')
class Truster(PrisonersDilemmaPersona):
    mutual_cooperation_strings = [
        'Good, I knew we were both reasonable!',
    ]

    betrayer_strings = [
        'I have no idea why I did this!',
        'I am not like this at all!',
    ]

    betrayee_strings = [
        'Jesus, why would you do this?',
        "I'm so disappointed!",
    ]

    mutual_betrayal_strings = [
        'Why have we done this to ourselves?',
    ]
    

@registry.register_persona(SimplePrisonersDilemma, 'v0')
class Sociopath(PrisonersDilemmaPersona):
    mutual_cooperation_strings = [
        'Good, I knew we were both reasonable!',
    ]

    betrayer_strings = [
        "I'm so sorry that you made this necessary",
    ]

    betrayee_strings = [
        'Jesus, why would you do this?',
        "I'm so disappointed!",
    ]

    mutual_betrayal_strings = [
        "I'll kill you for this!",
    ]


@registry.register_strategy(SimplePrisonersDilemma, 'v0')
class Cooperate(ConstantPolicy):
    action = 'cooperate'


@registry.register_strategy(SimplePrisonersDilemma, 'v0')    
class Defect(ConstantPolicy):
    action = 'defect'


@registry.register_strategy(SimplePrisonersDilemma, 'v0')    
class Random(RandomPolicy):
    actions = ['cooperate', 'defect']

