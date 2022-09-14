from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    forta = Forta.at(instance.forta())
    forta.setDetectionBot(attack, {'from': player})
