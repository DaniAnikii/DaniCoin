from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)


def P2PKH_scriptPubKey(address):
  
    return [
        OP_DUP,OP_HASH160,address,OP_EQUALVERIFY, OP_CHECKSIG
    ] 
    


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    
    return [
        signature, public_key
    ]
    ######################################################################

def send_from_P2PKH_transaction(amount_to_send, 
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey,
        sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0016064 - 0.0003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '36d0ca3a08b3bdd44cefb6c94c72efd45e38adf5d9cc99ac5155720f9f8eb97c')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)
    
    
    """
    
    OUTPUT:
    
    {
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "eb27fb57ff992dcea2cfebbfbb620424a49be91d5a7efe74d6e4a88280a17689",
    "addresses": [
      "mfZ2qPzRkvKY7c4i7VioaNa2YBvuRegKLN",
      "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
    ],
    "total": 130640,
    "fees": 30000,
    "size": 192,
    "vsize": 192,
    "preference": "high",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-24T08:39:23.916895913Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "36d0ca3a08b3bdd44cefb6c94c72efd45e38adf5d9cc99ac5155720f9f8eb97c",
        "output_index": 0,
        "script": "483045022100f3a2f4f38c8ee3b564b73d658d97ef1c7665a13bc868ee340d67f25b40b9c68402200baa92123ba1b0e412b692e2f9ef9d14a105b80f36c960278e3ce23d955a7fbc012103fade4e1e433ddea8e75ce34faa61d2940caa5be94217924b8c7181043f0a7368",
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
