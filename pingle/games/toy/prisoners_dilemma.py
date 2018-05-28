
from pingle import registry
from pingle.games.simultaneous_game import SimultaneousOneRoundGame
from pingle.policies.constant import ConstantPolicy
from pingle.policies.random import RandomPolicy

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
    
        
@registry.register_strategy(SimplePrisonersDilemma, 'v0')
class Cooperate(ConstantPolicy):
    action = 'cooperate'

    speech_act_matrix = {
        ('cooperate', 'cooperate'): (1, 1),
        ('cooperate', 'defect'): (1, 0),
        ('defect', 'cooperate'): (0, 1),
        ('defect', 'defect'): (0, 0),
    }
    
@registry.register_strategy(SimplePrisonersDilemma, 'v0')    
class Defect(ConstantPolicy):
    action = 'defect'

@registry.register_strategy(SimplePrisonersDilemma, 'v0')    
class Random(RandomPolicy):
    actions = ['cooperate', 'defect']

