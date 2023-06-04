import random
import requests
import threading
import time
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization

class KeyPair:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.public_key_hex = None
        self.generate_key_pair()

    def generate_key_pair(self):
        private_key = ed25519.Ed25519PrivateKey.generate()
        self.private_key = private_key
        self.public_key = private_key.public_key()
        self.public_key_hex = self.public_key.public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw
            ).hex()

def send_transaction_loop():

    # create 1000 addresses
    addresses = []
    for i in range(1000):
        key_pair = KeyPair()
        addresses.append(key_pair)

    while True:
        for i in range(1000):
            # Choisissez une adresse aléatoire
            recipient_address = random.choice(addresses).public_key_hex
            sender_address = addresses[i].public_key_hex

            data_to_sign = (str(sender_address) + str(recipient_address) + str(1)).encode()
            signature = addresses[i].private_key.sign(data_to_sign)


            try:
                # Construire la transaction
                # Remplacez les valeurs des adresses et des montants par les valeurs appropriées
                transaction_data = {
                    "sender_address": sender_address,
                    "recipient_address": recipient_address,
                    "amount": 1,
                    "signature": signature.hex()

                }

                # Envoyer la transaction à la blockchain
                response = requests.post("http://localhost:5000/transactions/new", json=transaction_data)

                if response.status_code == 200:
                    print("Transaction sent successfully!")
                else:
                    print("Failed to send transaction.")

            except Exception as e:
                print("Failed to send transaction.")

# Démarrez l'attaque dans un thread séparé
thread = threading.Thread(target=send_transaction_loop)
thread.start()
        
