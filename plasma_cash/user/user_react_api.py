#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:09:35 2019

@author: gaurava
"""
import configparser
import json
import os
from uuid import uuid4

from flask import Flask, request, jsonify
from flask.logging import default_handler
from flask_cors import CORS

from plasma_cash.user.user_class import User

os.system("clear")

# Instantiate the Node
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')


@app.route('/init_user', methods=['GET'])
def init_user():
    address = request.args.get('address')
    key = request.args.get('key')
    global user
    user = User(public_address=address, private_key=key)
    return 200


@app.route('/init_sc', methods=['POST'])
def init_sc():
    address = request.args.get('address')
    abi = request.args.get('abi')
    user.make_contract_object(_contract_address=address, _contract_abi=abi)
    return 200


@app.route('/deposit', methods=['GET'])
def deposit():
    try:
        print(request.args.get('amount'))
        _amount = int(request.args.get('amount'))
        print("s'dsd", _amount)
        print(user.deposit(amount=_amount))
        return jsonify(False), 200
    except:
        return jsonify(False), 201


@app.route('/validate', methods=['POST'])
def validate():
    try:
        address = request.form['address']
        key = request.form['privateKey']
        flag = User.validate_address(address, key)
        if flag:
            user.add_address(address, key)
        return jsonify(flag), 200
    except:
        return jsonify(False), 201


@app.route('/balance', methods=['GET'])
def balance():
    try:
        address = request.args.get('address')
        bal = user.get_balance(address)
        if bal is not None:
            return jsonify(bal), 200
    except:
        return jsonify("error"), 200


@app.route('/send_tx', methods=['GET'])
def send_tx():
    prev_block = request.form['prev_block']
    uid = request.form['uid']
    amount = request.form['amount']
    new_owner = request.form['new_owner']
    user.make_transfer(prev_block, uid, amount, new_owner)
    return 200


@app.route('/get_history/<uid>', methods=['GET'])
def get_history(uid):
    try:
        uid = int(uid)
        config = configparser.RawConfigParser()
        config.read(f'./{user.address}.properties')
        if not config.has_section("tokens"):
            return jsonify("uid not found"), 400
        if not config.has_option("tokens", str(uid)):
            return jsonify("uid not found", 400)
        block_num = int(config.get("tokens", str(uid)))

        txn = user.get_transaction(block_num, uid)
        response = dict()
        txn_details = {
            'prev_block': txn.prev_block,
            'uid': txn.uid,
            'amount': txn.amount,
            'new_owner': txn.new_owner.hex(),
        }
        response[block_num] = txn_details
        while txn.prev_block != 0:
            block_num = txn.prev_block
            txn = user.get_transaction(block_num, uid)
            txn_details = {
                'prev_block': txn.prev_block,
                'uid': txn.uid,
                'amount': txn.amount,
                'new_owner': txn.new_owner.hex()
            }
            response[block_num] = txn_details
        return jsonify(response), 200
    except:
        return jsonify("invalid uid "), 400


@app.route('/transfer/<uid>', methods=['GET'])
def transfer(uid):
    try:
        uid = int(uid)
        new_owner = request.args.get('new_owner')
        config = configparser.RawConfigParser()
        config.read(f'./{user.address}.properties')
        if not config.has_section("tokens"):
            return jsonify("uid not found"), 400
        if not config.has_option("tokens", str(uid)):
            return jsonify("uid not found", 400)
        block_num = int(config.get("tokens", str(uid)))
        print(block_num, new_owner)
        user.make_transfer(block_num, uid, 1, new_owner)
        return jsonify("transfer successfully done"), 200
    except:
        return jsonify("error occur"), 401


@app.route('/ping', methods=['GET'])
def get_address():
    data = {
        "address": user.address,
    }
    return jsonify(data), 200


@app.route('/sync_state', methods=['GET'])
def sync_state():
    """
    fetch -> last fetched block
    tokens -> uids owned by address
    metadata ->
    :return:
    """
    if not os.path.exists(f'./{user.address}.properties'):
        f = open(f'./{user.address}.properties', "w+")
        f.close()

    config = configparser.RawConfigParser()
    config.read(f'./{user.address}.properties')
    if not config.has_section("fetch"):
        config.add_section("fetch")
    if not config.has_section("tokens"):
        config.add_section("tokens")

    if not config.has_option("fetch", "last_block"):
        start_block = 1
    else:
        start_block = int(config.get("fetch", "last_block"))

    current_block = int(user.get_current_blk_num())
    user_address = str(user.address)[2:]
    user_address = user_address.lower()
    while start_block <= current_block:
        block = user.get_block(start_block)
        if block is not None:
            for txn in block.transaction_set:
                if str(txn.uid) in config.options("tokens"):
                    if int(txn.prev_block) == int(config.get("tokens", str(txn.uid))):
                        config.remove_option("tokens", str(txn.uid))
                # print(txn.new_owner.hex(), user_address)
                if txn.new_owner.hex() == user_address:
                    config.set("tokens", str(txn.uid), start_block)
        start_block = start_block + 1

    config.set("fetch", "last_block", str(current_block))
    file = open(f'./{user.address}.properties', 'w')
    config.write(file)
    file.close()
    response = {
        'tokens': config.items("tokens")
    }
    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5002, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    config = configparser.RawConfigParser()
    OWN_DIR = os.path.dirname(os.path.realpath(__file__))
    config.read(OWN_DIR + '/user.properties')

    eth_address = config.get('user', 'address')
    key = config.get('user', 'key')

    contract_address = config.get('contract', 'contract_address')

    _root_chain_provider = config.get('user', 'root_chain_provider')
    _side_chain_provider = config.get('user', 'side_chain_provider')
    user = User(public_address=eth_address, private_key=key, root_chain_provider=_root_chain_provider,
                child_chain_provider=_side_chain_provider)

    app.logger.removeHandler(default_handler)
    app.run(host='0.0.0.0', port=port)
