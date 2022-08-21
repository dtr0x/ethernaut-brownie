from scripts.level_helper import setup_instance

@setup_instance
def main(instance, player, attack):
    print(f'contract balance before: {instance.balanceOf(attack)}')
    print(f'player balance before: {instance.balanceOf(player)}')

    attack.run()

    print(f'contract balance after: {instance.balanceOf(attack)}')
    print(f'player balance after: {instance.balanceOf(player)}')
