from scripts.level_helper import setup_instance

@setup_instance
def main(instance, player, attack):
    attack.run({'from': player})
