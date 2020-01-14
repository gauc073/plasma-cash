"""
this file is created for web3.py basic operation understanding
"""
import json
from web3 import Web3
import requests
import rlp
from ethereum import utils
from web3.auto import w3

from plasma_cash.child_chain.block import Block
from plasma_cash.child_chain.transaction import Transaction
from plasma_cash.utils.utils import sign
web3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
print(web3.isConnected())
print(web3.eth.blockNumber)


account2 = '0xb75D453C47d1A432a6d056e2C8556612BD99b11F'
privateKey2 = 'f71190ee8450713bfeab9981d0f596d16e2fe64ee59ff25a94e959104c1b2277'

prevTxBlkNum = 1
tx_uid = 86808606383067142282285375973028804977544298667766506976594168911653156853950

contract_address = "0x1e1B6a8a85e848ed273d6D6Bb00A455809904CBa"
contract_address = web3.toChecksumAddress(contract_address)
bytecode = '608060405234801561001057600080fd5b506040516104213803806104218339818101604052602081101561003357600080fd5b81019080805164010000000081111561004b57600080fd5b8281019050602081018481111561006157600080fd5b815185602082028301116401000000008211171561007e57600080fd5b5050929190505050806000908051906020019061009c9291906100a3565b5050610115565b8280548282559060005260206000209081019282156100df579160200282015b828111156100de5782518255916020019190600101906100c3565b5b5090506100ec91906100f0565b5090565b61011291905b8082111561010e5760008160009055506001016100f6565b5090565b90565b6102fd806101246000396000f3fe608060405234801561001057600080fd5b50600436106100575760003560e01c80630a5868f81461005c5780632f265cf7146100a25780637021939f146100ea578063b13c744b14610132578063cc9ab26714610174575b600080fd5b6100886004803603602081101561007257600080fd5b81019080803590602001909291905050506101a2565b604051808215151515815260200191505060405180910390f35b6100ce600480360360208110156100b857600080fd5b81019080803590602001909291905050506101f8565b604051808260ff1660ff16815260200191505060405180910390f35b6101166004803603602081101561010057600080fd5b8101908080359060200190929190505050610234565b604051808260ff1660ff16815260200191505060405180910390f35b61015e6004803603602081101561014857600080fd5b8101908080359060200190929190505050610254565b6040518082815260200191505060405180910390f35b6101a06004803603602081101561018a57600080fd5b8101908080359060200190929190505050610275565b005b600080600090505b6000805490508110156101ed5782600082815481106101c557fe5b906000526020600020015414156101e05760019150506101f3565b80806001019150506101aa565b50600090505b919050565b6000610203826101a2565b61020c57600080fd5b6001600083815260200190815260200160002060009054906101000a900460ff169050919050565b60016020528060005260406000206000915054906101000a900460ff1681565b6000818154811061026157fe5b906000526020600020016000915090505481565b61027e816101a2565b61028757600080fd5b600180600083815260200190815260200160002060008282829054906101000a900460ff160192506101000a81548160ff021916908360ff1602179055505056fea265627a7a723058209e992f640d5bcdd758ee00e3dd3939eb57facd8188b51e5d0fa44f64c95a681b64736f6c63430005090032'
contract_abi = '[{"constant": false, "inputs": [{"name": "prevTx", "type": "bytes"}, {"name": "prevTxProof", "type": "bytes"}, {"name": "prevTxBlkNum", "type": "uint256"}, {"name": "tx", "type": "bytes"}, {"name": "txProof", "type": "bytes"}, {"name": "txBlkNum", "type": "uint256"}], "name": "startExit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "blkRoot", "type": "bytes32"}, {"name": "blknum", "type": "uint256"}, {"name": "isDepositBlock", "type": "bool"}, {"name": "depositTx", "type": "bytes"}, {"name": "depositTxProof", "type": "bytes"}], "name": "submitBlock", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "depositCount", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "uint256"}], "name": "exits", "outputs": [{"name": "hasValue", "type": "bool"}, {"name": "exitTime", "type": "uint256"}, {"name": "exitTxBlkNum", "type": "uint256"}, {"name": "exitTx", "type": "bytes"}, {"name": "txBeforeExitTxBlkNum", "type": "uint256"}, {"name": "txBeforeExitTx", "type": "bytes"}, {"name": "owner", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "uid", "type": "uint256"}], "name": "abortDeposit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "tx", "type": "bytes"}, {"name": "txProof", "type": "bytes"}, {"name": "txBlkNum", "type": "uint256"}], "name": "startDepositExit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "currency", "type": "address"}, {"name": "amount", "type": "uint256"}], "name": "deposit", "outputs": [{"name": "", "type": "uint256"}], "payable": true, "stateMutability": "payable", "type": "function"}, {"constant": false, "inputs": [{"name": "uid", "type": "uint256"}, {"name": "challengeTx", "type": "bytes"}, {"name": "proof", "type": "bytes"}, {"name": "blkNum", "type": "uint256"}], "name": "challengeExit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "uid", "type": "uint256"}, {"name": "challengeTx", "type": "bytes"}, {"name": "respondTx", "type": "bytes"}, {"name": "proof", "type": "bytes"}, {"name": "blkNum", "type": "uint256"}], "name": "respondChallengeExit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "currentBlkNum", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "uint256"}], "name": "wallet", "outputs": [{"name": "hasValue", "type": "bool"}, {"name": "isConfirmed", "type": "bool"}, {"name": "amount", "type": "uint256"}, {"name": "depositor", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "uid", "type": "uint256"}], "name": "finalizeExit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "authority", "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "uint256"}, {"name": "", "type": "uint256"}], "name": "challenges", "outputs": [{"name": "hasValue", "type": "bool"}, {"name": "challengeTx", "type": "bytes"}, {"name": "challengeTxBlkNum", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "uid", "type": "uint256"}, {"name": "challengeTx", "type": "bytes"}], "name": "isChallengeExisted", "outputs": [{"name": "", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "uint256"}], "name": "childChain", "outputs": [{"name": "", "type": "bytes32"}], "payable": false, "stateMutability": "view", "type": "function"}, {"inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "depositor", "type": "address"}, {"indexed": false, "name": "amount", "type": "uint256"}, {"indexed": false, "name": "uid", "type": "uint256"}], "name": "Deposit", "type": "event"}]'
contract_abi = json.loads(contract_abi)

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

authority = contract.functions.authority().call()
print(authority)


response = requests.get(f'http://localhost:8546/block/{prevTxBlkNum}')
block = rlp.decode(utils.decode_hex(response.content), Block)

tx = block.get_tx_by_uid(tx_uid)
block.merklize_transaction_set()
tx_proof = block.merkle.create_merkle_proof(tx_uid)

tx = contract.functions.startExit(
    rlp.encode(tx),
    tx_proof,
    prevTxBlkNum,
).buildTransaction({'from': account2})
tx['nonce'] = w3.eth.getTransactionCount(account2, 'pending')
privateKey2 = utils.normalize_key(privateKey2)
signed = w3.eth.account.signTransaction(tx, privateKey2)
txHash = w3.eth.sendRawTransaction(signed.rawTransaction)
# self._sign_and_send_tx(tx)
print(txHash)
