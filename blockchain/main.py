from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from blockchain import Blockchain
from memPool import MemPool



def main():

    blockchain = Blockchain([], 5, MemPool())
    blockchain.start()

if __name__ == "__main__":
    main()