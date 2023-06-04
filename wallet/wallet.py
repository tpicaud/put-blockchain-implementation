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

    # def load_private_key(self, password):
    #     # Charger encrypted_key à partir du fichier sécurisé
    #     self.private_key = serialization.load_pem_private_key(
    #         encrypted_key,
    #         password=password.encode()
    #     )
    #     self.public_key = self.private_key.public_key()

    def get_public_key(self):
        return self.public_key
    
    def send_transaction(self, recipient_address: str, amount: float):        
        signature_hex = self.get_signature(self.public_key_hex, recipient_address, amount).hex()
        transaction = Transaction(self.public_key_hex, recipient_address, amount, signature_hex)
        serialized_transaction = transaction.serialize()

        # Send the transaction to the blockchain
        response = requests.post("http://localhost:5000/transactions/new", json=serialized_transaction)
        if response.status_code == 200:
            print("Transaction sent successfully!")
        else:
            print("Failed to send transaction.")

    def get_signature(self, sender, recipient, amount) -> bytes:
        data_to_sign = str(sender).encode() + str(recipient).encode() + str(amount).encode()
        signature = self.private_key.sign(data_to_sign)
        return signature

# # Exemple d'utilisation
# wallet = Wallet()
# wallet.generate_key_pair()
# wallet.save_private_key("mot_de_passe")
# wallet.load_private_key("mot_de_passe")
# public_key = wallet.get_public_key()

# À partir d'ici, vous pouvez ajouter la fonctionnalité d'envoi de transactions en utilisant la clé privée du portefeuille.
