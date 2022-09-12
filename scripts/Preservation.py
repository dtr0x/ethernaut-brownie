from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    instance.setFirstTime(attack.address, {'from': player})
    instance.setFirstTime(player.address, {'from': player})

