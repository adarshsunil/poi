from BlockchainUtils import BlockchainUtils
from Lot import Lot


class ProofOfImmune():

    def __init__(self):
        self.karma = {}
        self.setGenesisNodeKarma()

    def setGenesisNodeKarma(self):
        genesisPublicKey = open('keys/genesisPublicKey.pem', 'r').read()
        self.karma[genesisPublicKey] = 1

    def update(self, publicKeyString, karma):
        if publicKeyString in self.karma.keys():
            self.karma[publicKeyString] += karma
        else:
            self.karma[publicKeyString] = karma

    def get(self, publicKeyString):
        if publicKeyString in self.karma.keys():
            return self.karma[publicKeyString]
        else:
            return None

    def validatorLots(self, seed):
        lots = []
        for validator in self.karma.keys():
            for karma in range(self.get(validator)):
                lots.append(Lot(validator, karma+1, seed))
        return lots

    def winnerLot(self, lots, seed):
        winnerLot = None
        leastOffset = None
        referenceHashIntValue = int(BlockchainUtils.hash(seed).hexdigest(), 16)
        for lot in lots:
            lotIntValue = int(lot.lotHash(), 16)
            offset = abs(lotIntValue - referenceHashIntValue)
            if leastOffset is None or offset < leastOffset:
                leastOffset = offset
                winnerLot = lot
        return winnerLot

    def karma(self, lastBlockHash):
        lots = self.validatorLots(lastBlockHash)
        winnerLot = self.winnerLot(lots, lastBlockHash)
        return winnerLot.publicKey

    def danger_score(karma_score, social_rep):
        danger = ((1-karma_score)*(1-social_rep))
        return danger
