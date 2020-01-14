import json

from flask import Blueprint, request

from generic.user_class import User
from plasma_cash.child_chain import event, websocket
from plasma_cash.dependency_config import container

child_chain = Blueprint('child_chain', __name__)
root_chain = Blueprint('root_chain', __name__)

clients = {}
user = None


@child_chain.route('/init_user', methods=['GET'])
def init_user():
    address = request.args.get('address')
    key = request.args.get('key')
    global user
    user = User(public_address=address, private_key=key)
    return 200


@child_chain.route('/init_sc', methods=['GET'])
def init_sc():
    address = request.args.get('address')
    abi = request.args.get('abi')
    user.make_contract_object(_contract_address=address, _contract_abi=abi)
    return 200


@child_chain.route('/send_tx', methods=['POST'])
def send_tx():
    prev_block = request.form['prev_block']
    uid = request.form['uid']
    amount = request.form['amount']
    new_owner = request.form['new_owner']
    user.make_transfer(prev_block, uid, amount, new_owner)
    return 200


@child_chain.route('/', methods=['GET'])
def init_user():
    address = request.args.get('address')
    key = request.args.get('key')
    user = User(public_address=address, private_key=key)
    return 200


@child_chain.route('', methods=['GET'])
def init_sc():
    address = request.args.get('address')
    abi = request.args.get('abi')
    user.make_contract_object(_contract_address=address, _contract_abi=abi)
    return 200


@child_chain.route('/', methods=['POST'])
def send_tx():
    prev_block = request.form['prev_block']
    uid = request.form['uid']
    amount = request.form['amount']
    new_owner = request.form['new_owner']
    user.make_transfer(prev_block, uid, amount, new_owner)
    return 200


@child_chain.route('/', methods=['GET'])
def init_user():
    address = request.args.get('address')
    key = request.args.get('key')
    user = User(public_address=address, private_key=key)
    return 200


@child_chain.route('', methods=['GET'])
def init_sc():
    address = request.args.get('address')
    abi = request.args.get('abi')
    user.make_contract_object(_contract_address=address, _contract_abi=abi)
    return 200


@child_chain.route('/', methods=['POST'])
def send_tx():
    prev_block = request.form['prev_block']
    uid = request.form['uid']
    amount = request.form['amount']
    new_owner = request.form['new_owner']
    user.make_transfer(prev_block, uid, amount, new_owner)
    return 200


@child_chain.route('/', methods=['GET'])
def init_user():
    address = request.args.get('address')
    key = request.args.get('key')
    user = User(public_address=address, private_key=key)
    return 200


@child_chain.route('', methods=['GET'])
def init_sc():
    address = request.args.get('address')
    abi = request.args.get('abi')
    user.make_contract_object(_contract_address=address, _contract_abi=abi)
    return 200


@child_chain.route('/', methods=['POST'])
def send_tx():
    prev_block = request.form['prev_block']
    uid = request.form['uid']
    amount = request.form['amount']
    new_owner = request.form['new_owner']
    user.make_transfer(prev_block, uid, amount, new_owner)
    return 200
