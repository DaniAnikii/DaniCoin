from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cQzA3bDU2BzzxEZkzquwovAgGoovg8s9wsCdKd7WLRjh6Lz28Nxh')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cPfYg2uqBEX68i1yeJoLhCvnfeE2HAFW2jY2vrg3wHYqkQtcC3bG')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cQDmQQ1mU7y2MbsmzQ1EY7C24NvKAE76VfeEtp2NoLS2ExbM3u2A')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
    	
    	#OP_3DUB,OP_3DUB,
        OP_NOT,
        OP_2, cust1_public_key, my_public_key, OP_2, OP_CHECKMULTISIG,
        OP_ELSE,
        OP_2, cust2_public_key, my_public_key, OP_2, OP_CHECKMULTISIG,
        OP_ELSE,
        OP_2, cust3_public_key, my_public_key, OP_2, OP_CHECKMULTISIG,
        OP_ENDIF,
        
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0016064 - 0.0003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '36d0ca3a08b3bdd44cefb6c94c72efd45e38adf5d9cc99ac5155720f9f8eb97c')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
    
    
    
  """
  
  OUTPUT:
  
  
  {
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "35fa4f606ecc5ae8d833bede24c86b34eaa0cc02306bd98be960afedcba5390c",
    "addresses": [
      "mfZ2qPzRkvKY7c4i7VioaNa2YBvuRegKLN"
    ],
    "total": 130640,
    "fees": 30000,
    "size": 383,
    "vsize": 383,
    "preference": "medium",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-25T08:06:01.364045492Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "36d0ca3a08b3bdd44cefb6c94c72efd45e38adf5d9cc99ac5155720f9f8eb97c",
        "output_index": 3,
        "script": "47304402207e9fe2bc490fd47882ce47dfafc7f0505f7d7d20e3845ef65f879263f4ae6c0502205895fe2f4d355ddd40ca9a4a78d5a2f8fb5629abb0ae8803d03a7d0795575521012103fade4e1e433ddea8e75ce34faa61d2940caa5be94217924b8c7181043f0a7368",
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
        "script": "6352210394c8e53cb08b53a9a94d2be2124605977bba2a07cb6be0b02151d960dbc31ef82103fade4e1e433ddea8e75ce34faa61d2940caa5be94217924b8c7181043f0a736852ae67522102ba65fb41dd0ff27e1abe49954da52cddd34702349a9aef9ce42168a60ebf3a7c2103fade4e1e433ddea8e75ce34faa61d2940caa5be94217924b8c7181043f0a736852ae67522102ca839239ac8c6d7a1e14c74a2a072511c7076d7932d6fbb4e522a77396400a7a2103fade4e1e433ddea8e75ce34faa61d2940caa5be94217924b8c7181043f0a736852ae68",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}
"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
