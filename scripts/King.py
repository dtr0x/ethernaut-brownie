from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    prize = instance.prize()
    attack.kingMe({'from': player, 'value': prize})
