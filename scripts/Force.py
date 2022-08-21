from scripts.level_helper import setup_instance

@setup_instance
def main(instance, player, attack):
    print(f'contact balance before: {instance.balance()}')
    attack.run({'from': player})
    print(f'contact balance after: {instance.balance()}')

