from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from ProofOfImmune import ProofOfImmune


class Blockchain():

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()
        self.poi = ProofOfImmune()

    def addBlock(self, block):
        self.executeTransactions(block.transactions)
        self.blocks.append(block)

    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data['blocks'] = jsonBlocks
        return data

    def blockCountValid(self, block):
        if self.blocks[-1].blockCount == block.blockCount - 1:
            return True
        else:
            return False

    def lastBlockHashValid(self, block):
        latestBlockchainBlockHash = BlockchainUtils.hash(
            self.blocks[-1].payload()).hexdigest()
        if latestBlockchainBlockHash == block.lastHash:
            return True
        else:
            return False

    def getCoveredTransactionSet(self, transactions):
        coveredTransactions = []
        for transaction in transactions:
            if self.transactionCovered(transaction):
                coveredTransactions.append(transaction)
            else:
                print('transaction is not covered by sender')
        return coveredTransactions

    def transactionCovered(self, transaction):
        if transaction.type == 'Self_score':
            return True
        senderBalance = self.accountModel.getBalance(transaction.senderPublicKey)
        if senderBalance >= transaction.amount:
            return True
        else:
            return False

    def executeTransactions(self, transactions):
        for transaction in transactions:
            self.executeTransaction(transaction)

    def executeTransaction(self, transaction):
        if transaction.type == 'KARMA':
            sender = transaction.senderPublicKey
            receiver = transaction.receiverPublicKey
            if sender == receiver:
                amount = transaction.amount
                self.poi.update(sender, amount)
                self.accountModel.updateBalance(sender, -amount)
        else:
            sender = transaction.senderPublicKey
            receiver = transaction.receiverPublicKey
            amount = transaction.amount
            self.accountModel.updateBalance(sender, -amount)
            self.accountModel.updateBalance(receiver, amount)

    def nextkarma(self):
        lastBlockHash = BlockchainUtils.hash(
            self.blocks[-1].payload()).hexdigest()
        nextkarma = self.poi.karma(lastBlockHash)
        return nextkarma

    def createBlock(self, transactionsFromPool, karmaWallet):
        coveredTransactions = self.getCoveredTransactionSet(
            transactionsFromPool)
        self.executeTransactions(coveredTransactions)
        newBlock = karmaWallet.createBlock(
            coveredTransactions, BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest(), len(self.blocks))
        self.blocks.append(newBlock)
        return newBlock

    def transactionExists(self, transaction):
        for block in self.blocks:
            for blockTransaction in block.transactions:
                if transaction.equals(blockTransaction):
                    return True
        return False

    def karmaValid(self, block):
        karmaPublicKey = self.poi.karma(block.lastHash)
        proposedBlockkarma = block.karma
        if karmaPublicKey == proposedBlockkarma:
            return True
        else:
            return False

    def transactionsValid(self, transactions):
        coveredTransactions = self.getCoveredTransactionSet(transactions)
        if len(coveredTransactions) == len(transactions):
            return True
        return False
