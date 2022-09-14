from brownie import *
import sys, os


def setup_instance(main):
   def main_wrapper():
       levelName = sys.argv[2] # get this from 'brownie run <levelName>'

       print(f'==================== Setting up {levelName} instance ====================')

       ethernaut = Ethernaut.deploy({'from': a[0]})
       level = eval(levelName + 'Factory').deploy({'from': a[0]})
       ethernaut.registerLevel(level)

       player = a[1]
       ethernaut.createLevelInstance(level, {'from': player, 'value': '0.001 ether'})
       if levelName not in {'PuzzleWallet', 'Motorbike'}:
           instance = eval(levelName).at(history[-1].new_contracts[0])
       else:
           instance = eval(levelName).at(history[-1].new_contracts[1])

       print('==================== Executing solution code ====================')

       if os.path.isfile(f'contracts/attacks/{levelName}Attack.sol'):
           attackContract = eval(levelName + 'Attack')
           constructorAbi = [i for i in attackContract.abi \
                             if i['type'] == 'constructor']

           if constructorAbi and \
                constructorAbi[0]['stateMutability'] == 'payable':
               value = '0.001 ether'
           else:
               value = 0

           if constructorAbi:
               attack = attackContract.deploy(\
                    instance, {'from': player, 'value': value})
           else:
               attack = attackContract.deploy(\
                    {'from': player, 'value': value})
       else:
           attack = None

       main(instance, player, attack)

       print('==================== Submitting level ====================')

       ethernaut.submitLevelInstance(instance, {'from': player})
       events = history[-1].events

       assert events and events.keys()[0] == 'LevelCompletedLog', \
            'Level submission did not pass check.'

       print('Level successfully passed.')

   return main_wrapper
