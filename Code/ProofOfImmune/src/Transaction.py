import uuid
import time
import copy


class Transaction():

    def __init__(self, senderPublicKey, receiverPublicKey, cp, type):
        self.senderPublicKey = senderPublicKey
        self.receiverPublicKey = receiverPublicKey
        self.cp = cp
        self.type = type
        self.id = (uuid.uuid1()).hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = signature

    def payload(self):
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation
    
    def danger_score(karma_score, social_rep):
        danger = ((1-karma_score)*(1-social_rep))
        return danger

   

    def equals(self, transaction):
        if self.id == transaction.id:
            return True
        else:
            return False
