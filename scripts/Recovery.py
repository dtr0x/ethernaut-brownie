from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    token = SimpleToken.at(history[-1].new_contracts[1])
    token.destroy(player, {'from': player})

