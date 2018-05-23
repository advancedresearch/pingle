from pingle import registry, tournament

prisoners_dilemma = registry.get_game_class('SimplePrisonersDilemma-v0')

cooperate = registry.make_strategy('SimplePrisonersDilemma-Cooperate-v0')
defect = registry.make_strategy('SimplePrisonersDilemma-Defect-v0')
random = registry.make_strategy('Random-v0')

tment = tournament.RoundRobinTwoPlayerTournament(
    games=[prisoners_dilemma],
    strategies=[cooperate, defect, random])


results = tment.run_tournament(num_rounds=1000)

print(results)
