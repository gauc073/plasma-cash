import rlp
from ethereum import utils
from web3.auto import w3
import time


from plasma_cash.client.client import Client
from plasma_cash.dependency_config import container
from plasma_cash.child_chain.block import Block
from plasma_cash.child_chain.transaction import Transaction
from plasma_cash.utils.utils import sign

import requests


def transferToken(prev_block, uid, amount, new_owner, owner_key):
    # client = Client(container.get_root_chain(), container.get_child_chain_client(), owner_key)
    # client.send_transaction(prev_block, uid, amount, new_owner)
    new_owner = utils.normalize_address(new_owner)
    tx = Transaction(prev_block, uid, amount, new_owner)
    owner_key = utils.normalize_key(owner_key)
    tx.sign(owner_key)
    # self.child_chain.send_transaction(rlp.encode(tx, Transaction).hex())
    encoded_txn = rlp.encode(tx, Transaction).hex()
    payload = {'tx': encoded_txn}

    response = requests.post("http://localhost:8546/send_tx", data=payload)
    print(response.status_code)
    if response.status_code == 200:
        print(response.content)


transferToken(1, 20839276404698775213859707403639915828445302135365795970937786894924151699657,
              4, '0xb75D453C47d1A432a6d056e2C8556612BD99b11F',
              '0x60bcab59317078ce0c4d36376ad692036215b615840711b1df8755350b362454')
# response = requests.get("http://localhost:8546/block/1")
# print("statuscode ", response.status_code)
# # print(type(response.content))
#
# tx = rlp.decode(utils.decode_hex(response.content), Block)
# print(tx)
#
# print(tx.merkle)
# for each in tx.transaction_set:
#     print(each)

# response = requests.get(f'http://{node_address}/chain')
#         response2 = requests.get(f'http://{node_address}/balance')
#         if response.status_code == 200:
#             remote_hash = response.json()['Hash']
#             remote_chain = response.json()['chain']
#             length = len(remote_chain)
#             utxo = response2.json()['utxo']
#

# payload = {'blknum':'3','uid':'123456'}
#
#
# response = requests.post('http://localhost:5002/proof', data=payload)