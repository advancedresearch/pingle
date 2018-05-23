# Hacky bullshit for now

GAME_REGISTRY = dict()

def get_game_class(game_name):
    return GAME_REGISTRY[game_name]
