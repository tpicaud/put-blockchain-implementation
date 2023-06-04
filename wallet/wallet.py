from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import requests

from transaction import Transaction

class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.public_key_hex = None
        

    def generate_key_pair(self):
        private_key = ed25519.Ed25519PrivateKey.generate()
        self.private_key = private_key
        self.public_key = private_key.public_key()
        self.public_key_hex = self.public_key.public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw
            ).hex()

    # def save_private_key(self, password):
    #     encrypted_key = self.private_key.private_bytes(
    #         encoding=serialization.Encoding.PEM,
    #         format=serialization.PrivateFormat.PKCS8,
    #         encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    #     )
    #     # Enregistrer encrypted_key dans un fichier sécurisé
    #     file_path = "wallet/encrypted_key.pem"
    #     with open(file_path, "wb") as file:
    #         file.write(encrypted_key)


    # def load_private_key(self, password):
    #     # Charger encrypted_key à partir du fichier sécurisé
    #     file_path = "wallet/encrypted_key.pem"
    #     with open(file_path, "rb") as file:
    #         encrypted_key = file.read()

    #     self.private_key = serialization.load_pem_private_key(
    #         encrypted_key,
    #         password=password.encode()
    #     )
    #     self.public_key = self.private_key.public_key()

    def get_public_key(self):
        return self.public_key
    
    def get_public_key_hex(self):
        return self.public_key_hex
    
    def send_transaction(self, recipient_address: str, amount: float):    
        # Check current balance
        try: 
            balance = self.get_balance()
            if balance < amount:
                print("Insufficient funds.")
                return
            elif amount <= 0:
                print("Invalid amount.")
                return
            elif recipient_address == self.public_key_hex:
                print("You can't send money to yourself.")
                return
            else:
                # Sign the transaction
                signature_hex = self.sign(self.public_key_hex, recipient_address, amount).hex()
                transaction = Transaction(self.public_key_hex, recipient_address, amount, signature_hex)
                serialized_transaction = transaction.serialize()

                # Send the transaction to the blockchain
                try:
                    response = requests.post("http://localhost:5000/transactions/new", json=serialized_transaction)
                    if response.status_code == 200:
                        print("Transaction sent successfully!")
                    else:
                        print("Failed to send transaction.")
                except Exception as e:
                    print("Failed to send transaction.")
                    return
        except Exception as e:
            print("Failed to send transaction.")
            return

    def get_balance(self, address: str = None) -> float:
        if address is None:
            address = self.public_key_hex
        try:
            response = requests.get("http://localhost:5000/balance/" + address)
            balance = response.json()['balance']
            return balance
        except Exception as e:            
            print("Failed to get current balance.")
            return

    def sign(self, sender, recipient, amount) -> bytes:
        data_to_sign = str(sender).encode() + str(recipient).encode() + str(amount).encode()
        signature = self.private_key.sign(data_to_sign)
        return signature