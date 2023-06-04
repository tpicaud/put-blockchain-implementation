from flask import Flask, request, jsonify
from transaction import Transaction
class Controller:
    def __init__(self, _blockchain):
        self.app = Flask(__name__)
        self.blockchain = _blockchain

        # Register routes
        self.register_routes()

    def register_routes(self):
        # Endpoint for receiving new transactions
        self.app.route('/transactions/new', methods=['POST'])(self.receive_transaction)
        self.app.route('/balance/<address>', methods=['GET'])(self.get_balance)

    def receive_transaction(self):
        try:
            transaction_data = request.get_json()
            sender_address = transaction_data['sender_address']
            recipient_address = transaction_data['recipient_address']
            amount = transaction_data['amount']
            signature = transaction_data['signature']

            transaction = Transaction(sender_address, recipient_address, amount, signature)
            self.blockchain.receiveTransaction(transaction)

            return jsonify({'message': 'Transaction received and sent to mempool.'}), 200
        except Exception as e:
            return jsonify({'message': 'Invalid transaction format.'}), 400
        
    def get_balance(self, address):
        try:
            balance = self.blockchain.get_balance(address)
            return jsonify({'balance': balance}), 200
        except:
            return jsonify({'message': 'Invalid address format.'}), 400
    

    def run(self):
        ## Disable logs
        import logging
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        ## Run the app
        self.app.run()