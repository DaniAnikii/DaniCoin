from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2


Q2a_txout_scriptPubKey = [
       OP_2DUP, OP_ADD, 18, OP_EQUALVERIFY,OP_SUB,16,OP_EQUAL
    ]
######################################################################

if __name__ == '__main__':
   
    amount_to_send = 0.0016064 - 0.0003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '36d0ca3a08b3bdd44cefb6c94c72efd45e38adf5d9cc99ac5155720f9f8eb97c')
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
    
"""


OUTPUT:

{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "6ad185a696e64d31b17bead97ce254088065ca5fc0986eb3577d02504cc90155",
    "addresses": [
      "mfZ2qPzRkvKY7c4i7VioaNa2YBvuRegKLN"
    ],
    "total": 130640,
    "fees": 30000,
    "size": 174,
    "vsize": 174,
    "preference": "high",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-24T10:02:20.787421809Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "36d0ca3a08b3bdd44cefb6c94c72efd45e38adf5d9cc99ac5155720f9f8eb97c",
        "output_index": 1,
        "script": "473044022030865bb4b496b440a82787b5b1c249c36a78db4e45c28b39b03c63ab4970ffae0220575ab0060dffa74a4a43305610800023dc623555f7ec96177f370a40202a4d45012103fade4e1e433ddea8e75ce34faa61d2940caa5be94217924b8c7181043f0a7368",
        "output_value": 160640,
        "sequence": 4294967295,
        "addresses": [
          "mfZ2qPzRkvKY7c4i7VioaNa2YBvuRegKLN"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2377959
      }
    ],
    "outputs": [
      {
        "value": 130640,
        "script": "6e93011288946087",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}

"""
