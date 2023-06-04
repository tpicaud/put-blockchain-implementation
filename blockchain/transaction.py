from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

# sender: hexadecimal representation of the public key of the sender
# recipient: hexadecimal representation of the public key of the recipient
# amount: amount of coins to be transferred
# signature: hexadecimal representation of the signature of the transaction
class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float, signature: str) :
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature
    
    def isValid(self) -> bool:
        try:
            signature_in_bytes = bytes.fromhex(self.signature)
            data = self.sender.encode() + self.recipient.encode() + str(self.amount).encode()

            sender_public_key = bytes.fromhex(self.sender)
            public_key = ed25519.Ed25519PublicKey.from_public_bytes(sender_public_key)
            public_key.verify(signature_in_bytes, data)
        except Exception as e:
            print("Erreur :", e)
            return False
        return True
