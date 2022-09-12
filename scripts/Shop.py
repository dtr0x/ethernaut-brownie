from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    attack.buy({'from': player})

