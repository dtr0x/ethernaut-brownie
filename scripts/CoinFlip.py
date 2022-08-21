from scripts.level_helper import setup_instance

@setup_instance
def main(instance, player, attack):
    for i in range(10):
        attack.run()
