from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests


def postTransaction(sender, receiver, cp, type):
    transaction = sender.createTransaction(receiver.publicKeyString(), cp, type)
    url = "http://localhost:5000/transaction"
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)


if __name__ == '__main__':

    bob = Wallet()
    alice = Wallet()
    alice.fromKey('keys/stakerPrivateKey.pem')
    Self_score = Wallet()

    #karma: genesis
    postTransaction(Self_score, alice, 1, 'Self_score')
    postTransaction(Self_score, bob, 1, 'Self_score')
    postTransaction(Self_score, bob, 1, 'Self_score')

    # karma: probably alice
    postTransaction(alice, alice, 0.25, 'KARMA')
    postTransaction(alice, bob, 1, 'Social_reputation')
    postTransaction(alice, bob, 1, 'Social_reputation')

#simulation for running transactions