from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

# sender: hexadecimal representation of the public key of the sender
# recipient: hexadecimal representation of the public key of the recipient
# amount: amount of coins to be transferred
# signature: hexadecimal representation of the signature of the transaction
class Transaction:
    def __init__(self, sender_adress: str, recipient_adress: str, amount: int, signature: str) :
        self.sender_address = sender_adress
        self.recipient_address = recipient_adress
        self.amount = amount
        self.signature = signature
    
    def serialize(self):
        return {
            "sender_address": self.sender_address,
            "recipient_address": self.recipient_address,
            "amount": self.amount,
            "signature": self.signature
        }