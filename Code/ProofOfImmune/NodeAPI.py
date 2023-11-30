from flask import Flask, jsonify, request
from flask.views import MethodView
from BlockchainUtils import BlockchainUtils

node = None
app = Flask(__name__)

class NodeAPI(MethodView):

    @staticmethod
    def start(port):
        app.run(host='localhost', port=port)

    @staticmethod
    def injectNode(injectedNode):
        global node
        node = injectedNode

    def get(self, path):
        if path == "info":
            return self.info()
        elif path == "blockchain":
            return self.blockchain()
        elif path == "transactionPool":
            return self.transactionPool()

    def post(self, path):
        if path == "transaction":
            return self.transaction()

    def info(self):
        return 'This is a communication interface to a node\'s blockchain', 200

    def blockchain(self):
        return node.blockchain.toJson(), 200

    def transactionPool(self):
        transactions = {}
        for ctr, transaction in enumerate(node.transactionPool.transactions):
            transactions[ctr] = transaction.toJson()
        return jsonify(transactions), 200

    def transaction(self):
        values = request.get_json()
        if not 'transaction' in values:
            return 'Missing transaction value', 400
        transaction = BlockchainUtils.decode(values['transaction'])
        node.handleTransaction(transaction)
        response = {'message': 'Received transaction'}
        return jsonify(response), 201

# Register the class with specific routes
node_view = NodeAPI.as_view('node_api')
app.add_url_rule('/<path:path>', view_func=node_view, methods=['GET', 'POST'])
