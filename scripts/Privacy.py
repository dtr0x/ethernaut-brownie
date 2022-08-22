from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    key = web3.eth.getStorageAt(instance.address, 5).zfill(32)[:16]
    instance.unlock(key, {'from': player})

