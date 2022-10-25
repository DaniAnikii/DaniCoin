from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q2a import Q2a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0013064 - 0.0003 # amount of BTC in the output you're sending minus fee
txid_to_spend = (
        '6ad185a696e64d31b17bead97ce254088065ca5fc0986eb3577d02504cc90155')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a.
txin_scriptSig = [
        17,1
]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)

"""

OUTPUT:

{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "47d432cc3a106bd87963796926454b29497febc72ef13a051ab143f7a5ce7952",
    "addresses": [
      "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
    ],
    "total": 100640,
    "fees": 30000,
    "size": 88,
    "vsize": 88,
    "preference": "high",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-24T10:04:32.028152981Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "6ad185a696e64d31b17bead97ce254088065ca5fc0986eb3577d02504cc90155",
        "output_index": 0,
        "script": "011151",
        "output_value": 130640,
        "sequence": 4294967295,
        "script_type": "unknown",
        "age": 0
      }
    ],
    "outputs": [
      {
        "value": 100640,
        "script": "76a9149f9a7abd600c0caa03983a77c8c3df8e062cb2fa88ac",
        "addresses": [
          "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
        ],
        "script_type": "pay-to-pubkey-hash"
      }
    ]
  }
}


"""
