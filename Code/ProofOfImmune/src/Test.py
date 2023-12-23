from ProofOfImmune import ProofOfImmune
from Lot import Lot
import string
import random


def getRandomString(length):
    letters = string.ascii_lowercase
    resultString = ''.join(random.choice(letters) for i in range(length))
    return resultString


if __name__ == '__main__':
    poi = ProofOfImmune()
    poi.update('bob', 100)
    poi.update('alice', 100)

    bobWins = 0
    aliceWins = 0

    for i in range(100):
        karma = poi.karma(getRandomString(i))
        if karma == 'bob':
            bobWins += 1
        elif karma == 'alice':
            aliceWins += 1

    print('Bob won: ' + str(bobWins) + ' times')
    print('Alice won: ' + str(aliceWins) + ' times')
