from generic.user_class import User
import json
import time


def block_explorer(_block):
    if _block is None:
        return
    print("---block explorer---")
    transaction_count = len(_block.transaction_set)
    print(transaction_count)
    for txn in _block.transaction_set:
        transaction_explorer(txn)
    print("--------------------")


def transaction_explorer(transaction):
    print('prev_block', transaction.prev_block),
    print('uid', transaction.uid),
    print('amount', transaction.amount),
    print('new_owner', transaction.new_owner.hex()),
    print('sig', transaction.sig)


CG = User("0x34Cf529D3932B274693dC73754f62eB97d25D875",
          "0x60bcab59317078ce0c4d36376ad692036215b615840711b1df8755350b362454")

contract_address = "0xB9454B9eD41Fb973Cd6CC25C4B99d1CE2a163c86"
contract_abi = '[{"constant": false, "inputs": [{"name": "prevTx", "type": "bytes"}, {"name": "prevTxProof", "type": "bytes"}, {"name": "prevTxBlkNum", "type": "uint256"}, {"name": "tx", "type": "bytes"}, {"name": "txProof", "type": "bytes"}, {"name": "txBlkNum", "type": "uint256"}], "name": "startExit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "blkRoot", "type": "bytes32"}, {"name": "blknum", "type": "uint256"}, {"name": "isDepositBlock", "type": "bool"}, {"name": "depositTx", "type": "bytes"}, {"name": "depositTxProof", "type": "bytes"}], "name": "submitBlock", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "depositCount", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "uint256"}], "name": "exits", "outputs": [{"name": "hasValue", "type": "bool"}, {"name": "exitTime", "type": "uint256"}, {"name": "exitTxBlkNum", "type": "uint256"}, {"name": "exitTx", "type": "bytes"}, {"name": "txBeforeExitTxBlkNum", "type": "uint256"}, {"name": "txBeforeExitTx", "type": "bytes"}, {"name": "owner", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "uid", "type": "uint256"}], "name": "abortDeposit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "tx", "type": "bytes"}, {"name": "txProof", "type": "bytes"}, {"name": "txBlkNum", "type": "uint256"}], "name": "startDepositExit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "currency", "type": "address"}, {"name": "amount", "type": "uint256"}], "name": "deposit", "outputs": [{"name": "", "type": "uint256"}], "payable": true, "stateMutability": "payable", "type": "function"}, {"constant": false, "inputs": [{"name": "uid", "type": "uint256"}, {"name": "challengeTx", "type": "bytes"}, {"name": "proof", "type": "bytes"}, {"name": "blkNum", "type": "uint256"}], "name": "challengeExit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "uid", "type": "uint256"}, {"name": "challengeTx", "type": "bytes"}, {"name": "respondTx", "type": "bytes"}, {"name": "proof", "type": "bytes"}, {"name": "blkNum", "type": "uint256"}], "name": "respondChallengeExit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "currentBlkNum", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "uint256"}], "name": "wallet", "outputs": [{"name": "hasValue", "type": "bool"}, {"name": "isConfirmed", "type": "bool"}, {"name": "amount", "type": "uint256"}, {"name": "depositor", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "uid", "type": "uint256"}], "name": "finalizeExit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "authority", "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "uint256"}, {"name": "", "type": "uint256"}], "name": "challenges", "outputs": [{"name": "hasValue", "type": "bool"}, {"name": "challengeTx", "type": "bytes"}, {"name": "challengeTxBlkNum", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "uid", "type": "uint256"}, {"name": "challengeTx", "type": "bytes"}], "name": "isChallengeExisted", "outputs": [{"name": "", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "uint256"}], "name": "childChain", "outputs": [{"name": "", "type": "bytes32"}], "payable": false, "stateMutability": "view", "type": "function"}, {"inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "depositor", "type": "address"}, {"indexed": false, "name": "amount", "type": "uint256"}, {"indexed": false, "name": "uid", "type": "uint256"}], "name": "Deposit", "type": "event"}]'
contract_abi = json.loads(contract_abi)

CG.make_contract_object(contract_address, contract_abi)

uid = 20839276404698775213859707403639915828445302135365795970937786894924151699657

# print("authority->,", CG.get_authority())
# print("current block number ", CG.get_current_blk_num())
# print("deposit count ", CG.get_deposit_count())
# print("merkle root of block 12 ", CG.get_merkle_root(12).hex())
# print("exits for uid ", CG.get_exits(uid))
# print("wallet for uid ", CG.get_wallet(uid))
# print("challenge ", CG.get_challenges(uid, 0))

# tx_hash = CG.deposit(2).hex()
# time.sleep(3)


# print("getblock ", CG.get_block())
# block_explorer(CG.get_block(2))
# print("get proof ", CG.get_proof(1, uid))
# print("get transaction ", CG.get_transaction(1, 93593935279807735542589239940852641400675421943886570363382826313195688356508))
# tx_hash = "0x9e94f87e3c44b5427b7176eaf1a48e21b55a4a447b200ad4cfd8cd8b506a0dca"
# print(CG.get_uid(0xb1790ea57981623d37d2ecd34bbf250053802a1faa0fadb08f67127c5e1a24a7))
# blk_num =CG.get_block_num(93593935279807735542589239940852641400675421943886570363382826313195688356508)
# print(blk_num)
# print("get transaction ", CG.get_transaction(blk_num, 93593935279807735542589239940852641400675421943886570363382826313195688356508).prev_block)
# print(CG.get_block_num(82182828661148063140671830436521161190402484120131272455366403615756934218076))

# 0x456b2995e2b72f1797a0ce1f41fa9a7e0e32bee5aec8031530ed2e7aa97032b1

# num = CG.get_block_num(34245301184389696679752638244440167881132627060124604433654081881323948637572)
# block_explorer(CG.get_block(num))
# block_explorer(CG.get_block(num-1))
# block_explorer(CG.get_block(num+1))

block_explorer(CG.get_block(915))