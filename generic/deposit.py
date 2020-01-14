import time
import sys
from behave import given, then, when
from web3.auto import w3

from integration_tests.features.utils import address_equals, has_value
from plasma_cash.client.client import Client
from plasma_cash.dependency_config import container

eth_currency = '0x0000000000000000000000000000000000000000'


def deposit_eth_to_plasma(user_key, amount):
    client = Client(container.get_root_chain(), container.get_child_chain_client(), user_key)
    client.deposit(amount=amount, currency=eth_currency)
    time.sleep(5)


"""
sys arguments:-
    :arg[1] user_address
    :arg[2] user_key 
    :arg[3] amount
"""
if sys.argv[1] is None or sys.argv[2] is None or sys.argv[3] is None:
    print("please provide input(s)")
# try:
address = w3.toChecksumAddress(sys.argv[1])
deposit_amount = int(sys.argv[3])
userA_balance = w3.eth.getBalance(address)
userA_balance = userA_balance/ (10**18)
print(userA_balance)
print(deposit_amount)
print(type(deposit_amount))
if userA_balance > int(sys.argv[3]):
    deposit_eth_to_plasma(sys.argv[2], deposit_amount)
else:
    print("raise error: insufficient balance")
# except:
#     print("error occur in process, not able to deposit")