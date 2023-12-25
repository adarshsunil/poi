from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests


def postTransaction(sender, receiver, karma_score, social_rep, type):
    transaction = sender.createTransaction(receiver.publicKeyString(), karma_score, social_rep, type)
    url = "http://localhost:5000/transaction"
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)


if __name__ == '__main__':

    bob = Wallet()
    alice = Wallet()
    alice.fromKey('keys/karmaPrivateKey.pem')
    Self_score = Wallet()

    #karma: genesis
    postTransaction(Self_score, alice, 1, 1, 'Self_score')
    postTransaction(Self_score, bob, 1, 1, 'Self_score')
    postTransaction(Self_score, bob, 1,1, 'Self_score')

    # karma: probably alice
    postTransaction(alice, alice, 2, 1, 'KARMA')
    postTransaction(alice, bob, 3,1,  'Social_reputation')
    postTransaction(alice, bob, 1, 1,'Social_reputation')

#simulation for running transactions
