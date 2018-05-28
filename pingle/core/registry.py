# Hacky bullshit for now

GAME_REGISTRY = dict()
STRATEGY_REGISTRY = dict()

def get_game_class(game_name):
    assert game_name in GAME_REGISTRY, str(GAME_REGISTRY)
    return GAME_REGISTRY[game_name]


def make_strategy(strategy_name):
    assert strategy_name in STRATEGY_REGISTRY, \
        strategy_name + '\n' + str(STRATEGY_REGISTRY)
    return_value = STRATEGY_REGISTRY[strategy_name]()
    return_value.name = strategy_name
    return return_value

def register_game(version):
    def decorator(game_class):
        name = str(game_class.__name__) + '-' + version
        GAME_REGISTRY[name] = game_class
        return game_class
    return decorator


def register_strategy(game_class, version):
    def decorator(strategy_class):
        name = '-'.join([str(game_class.__name__),
                         str(strategy_class.__name__),
                         version])
        STRATEGY_REGISTRY[name] = strategy_class
        return strategy_class
    return decorator
