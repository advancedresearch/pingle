from pingle import registry
from pingle.tournaments import round_robin

prisoners_dilemma = registry.get_game_class('SimplePrisonersDilemma-v0')

cooperate = registry.make_strategy('SimplePrisonersDilemma-Cooperate-v0')
defect = registry.make_strategy('SimplePrisonersDilemma-Defect-v0')
random = registry.make_strategy('SimplePrisonersDilemma-Random-v0')

tournament = round_robin.RoundRobinTwoPlayerTournament(
    games=[prisoners_dilemma],
    strategies=[cooperate, defect, random])


tournament.run_tournament(num_rounds=1000)

