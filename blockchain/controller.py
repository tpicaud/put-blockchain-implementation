from flask import Flask, request, jsonify
from transaction import Transaction
import time

class Controller:
    def __init__(self, _blockchain):
        self.app = Flask(__name__)
        self.blockchain = _blockchain

        # Dictionary to store the last transaction timestamp per IP address
        self.last_transaction_times = {}

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

            # Check if the IP address has exceeded the transaction frequency limit
            client_ip = request.remote_addr
            if not self.can_send_transaction(client_ip):
                return jsonify({'message': 'Too many transactions from this IP address. Please try again later.'}), 429

            transaction = Transaction(sender_address, recipient_address, amount, signature)
            self.blockchain.receiveTransaction(transaction)

            # Update the last transaction time for the IP address
            self.last_transaction_times[client_ip] = time.time()

            return jsonify({'message': 'Transaction received and sent to mempool.'}), 200
        except Exception as e:
            return jsonify({'message': 'Invalid transaction format.'}), 400

    def can_send_transaction(self, client_ip):
        # Check if the IP address has sent a transaction within the last 10 seconds
        last_time = self.last_transaction_times.get(client_ip, 0)
        return (time.time() - last_time) > 2

    def get_balance(self, address):
        try:
            balance = self.blockchain.get_balance(address)
            return jsonify({'balance': balance}), 200
        except:
            return jsonify({'message': 'Invalid address format.'}), 400

    def run(self):
        # Disable logs
        import logging
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        # Run the app
        self.app.run()
