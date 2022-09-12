from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    instance.setWithdrawPartner(attack, {'from': player})
    pass

