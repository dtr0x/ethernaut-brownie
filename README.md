# ethernaut-brownie
Solutions to [Ethernaut](https://ethernaut.openzeppelin.com/) challenges using the [Brownie](https://eth-brownie.readthedocs.io/en/stable/) framework. 

The code does not interact with the Rinkeby network, and instead sets up a development fork of Rinkeby. See the Brownie documentation for instructions on how to do this. This has several benefits including speed, not having to obtain test ether, and allowing the game to be played using just the command line.

## Setup
```
brownie pm install OpenZeppelin/openzeppelin-contracts@3.2.0
brownie pm install OpenZeppelin/openzeppelin-contracts-upgradeable@4.2.0
```

## Usage
All level submissions happen via a python script in `scripts/<LevelName>.py` derived from `scripts/challenge_template.py`. This includes a `main` function decorated with additional logic from `scripts/level_helper.py`, which sets up the Ethernaut contract on the forked testnet, generates a level instance and finally submits the level after the `<LevelName>.py` script completes. Some levels use just a script to obtain a solution, if a contract is used it is assumed to be located at `contracts/attacks/<LevelName>Attack.sol`.

To run the solution for a particular level, execute the following from the top-level directory:
```
brownie run <LevelName>
```
where `<LevelName>` is any of
```
Fallback, Fallout, CoinFlip, Telephone, Token, Delegation, Force, Vault, King, Reentrance, 
Elevator, Privacy, GatekeeperOne, GatekeeperTwo, NaughtCoin, Preservation, Recovery, MagicNum, 
AlienCodex, Denial, Shop, Dex, DexTwo, PuzzleWallet, Motorbike, DoubleEntryPoint, GoodSamaritan
```



