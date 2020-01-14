import rlp
from ethereum import utils
from web3.auto import w3

from plasma_cash.child_chain.block import Block
from plasma_cash.child_chain.transaction import Transaction
from plasma_cash.utils.utils import sign

import requests


blknum = 1
print(blknum)
response = requests.get(f'http://localhost:8546/block/{blknum}')
# print("statusecode ", response.status_code)
# print(type(response.content))

block = rlp.decode(utils.decode_hex(response.content), Block)
# print(block)

# print("block_hash ", block.hash)
for each_tx in block.transaction_set:
    print("tx hash ", each_tx)
    print("tx uid ", each_tx.uid)
    payload = {'blknum': blknum, 'uid': each_tx.uid}
    r = requests.get('http://localhost:8546/proof', params=payload)
    # print("proof status code", r.status_code)
    if r.status_code == 200:
        print(type(r.content))

# response = requests.get(f'http://{node_address}/chain')
#         response2 = requests.get(f'http://{node_address}/balance')
#         if response.status_code == 200:
#             remote_hash = response.json()['Hash']
#             remote_chain = response.json()['chain']
#             length = len(remote_chain)
#             utxo = response2.json()['utxo']
#   b'8N\xf1F\x17\xbb&\xc2\xab|\xfb\xd2\xd4k[1\xeb\x0bo\x15D\xb7\xf2\x0b\xf2\xfblug\xb8\xb2\xa4'