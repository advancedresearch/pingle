from pingle import registry, tournaments

iterated_prisoners_dilemma = registry.get_game_class(
    'IteratedPrisonersDilemma-v0')

cooperate = registry.make_strategy(
    'IteratedPrisonersDilemma-Cooperate-v0')
defect = registry.make_strategy(
    'IteratedPrisonersDilemma-Defect-v0')
random = registry.make_strategy(
    'IteratedPrisonersDilemma-Random-v0')
tit_for_tat = registry.make_strategy(
    'IteratedPrisonersDilemma-TitForTat-v0')
tit_for_tat_forgive = registry.make_strategy(
    'IteratedPrisonersDilemma-TitForTatForgive-v0')

tment = tournament.RoundRobinTwoPlayerTournament(
    games=[iterated_prisoners_dilemma],
    strategies=[cooperate,
                defect,
                random,
                tit_for_tat,
                tit_for_tat_forgive])


tment.run_tournament(num_rounds=1000)

