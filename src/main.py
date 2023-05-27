from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from transaction import Transaction


def main():
    private_key1 = ed25519.Ed25519PrivateKey.generate()
    public_key1 = private_key1.public_key()
    private_key2 = ed25519.Ed25519PrivateKey.generate()
    public_key2 = private_key2.public_key()

    # Exemple de transaction valide
    sender_hex = public_key1.public_bytes(encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw).hex()
    recipient_hex = public_key2.public_bytes(encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw).hex()
    amount = 100
    data_to_sign = sender_hex.encode() + recipient_hex.encode() + str(amount).encode()
    signature = private_key1.sign(data_to_sign)


    transaction =   Transaction(sender_hex, recipient_hex, amount, signature.hex())
    print("Transaction valide :", transaction.isValid())

    # Exemple de transaction invalide (signature incorrecte)
    sender = 'f2ae3d6f4fc1b29f41e4065e7efb0be2bda1d2d33e0e9d4501e842b3e4a38d24'
    recipient = 'ae6e6f0e0a914e52ac4a1dc481c196b9f3ebab21b9ff49a345bc036e4d9f352d'
    amount = 100
    signature = 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
    hash = 'abcdef1234567890'

    transaction = Transaction(sender, recipient, amount, signature)
    print("Transaction valide :", transaction.isValid())

if __name__ == "__main__":
    main()