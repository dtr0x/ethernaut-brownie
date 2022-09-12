from scripts.level_helper import *

@setup_instance
def main(instance, player, attack):
    # run solc --strict-assembly contracts/attacks/Solver.yul | grep -A1 "Binary representation:" to get this bytecode
    bytecode = '0x33600055600a6011600039600a6000f3fe602a60005260206000f3'
    la = accounts.add()
    a[0].transfer(la, '10 ether')
    signed_txn = web3.eth.account.sign_transaction({
        'nonce': 0,
        'gasPrice': Wei('10 gwei'),
        'gas': 100000,
        'data': bytecode
    }, la.private_key)
    tx = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    contract = web3.eth.get_transaction_receipt(tx)['contractAddress']
    fnsig = web3.keccak(text='whatIsTheMeaningOfLife()')[:4].hex()
    val = int(web3.eth.call({'from': la.address, 'to': contract, 'data': fnsig}).hex(), 16)
    print(f'The meaning of life is {val}')

    instance.setSolver(contract, {'from': player})
