import hashlib

from typing import List
from transaction import Transaction

class Block:
    def __init__(self, index: int, timestamp: int, transactions: List[Transaction], previous_hash:str) :
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions.copy() # Copy the list of transactions to avoid deletion by reference
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self) -> str:
        ## Calculate the hash of the block
        block_string = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mineBlock(self, difficulty: int) :
        target = "0" * difficulty
        while self.hash[0:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculateHash()
        

    def hasValidTransactions(self) -> bool:
        ## Check if all transactions in the block are valid
        for transaction in self.transactions:
            if not transaction.isValid():
                return False
        return True