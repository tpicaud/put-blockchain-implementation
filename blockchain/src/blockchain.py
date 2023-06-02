import datetime
import threading
import time
from typing import List
from block import Block
from memPool import MemPool
from transaction import Transaction

class Blockchain:
    def __init__(self, chain: List[Block], difficulty: int, mem_pool: MemPool) -> None:
        self.chain = chain
        self.difficulty = difficulty
        self.mem_pool = mem_pool

    def addBlock(self, transactions: List[Transaction]) :
        if len(self.chain) == 0:
            # Genesis block
            previous_hash = "0"
            block = Block(0, self.get_current_timestamp(), [], previous_hash)
        else:
            # New block
            previous_block = self.chain[-1]
            block = Block(previous_block.index + 1, self.get_current_timestamp(), transactions, previous_block.hash)
            block.mineBlock(self.difficulty)
        self.chain.append(block)

    def isValid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if the current block hash is correct
            if current_block.hash != current_block.calculateHash():
                return False

            # Check if the previous block hash is correct
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def get_current_timestamp(self) -> int:
        current_datetime = datetime.datetime.now()
        timestamp = int(current_datetime.timestamp())
        return timestamp
    
    def start(self) -> None:
        print("\n                 Starting blockchain UI...")
        print("-----------------------------------------------------------\n")
        while True:
            self.addBlock(self.mem_pool.getTransactions())
            self.printBlock(self.chain[-1])    

    def printBlock(self, block) -> None:
        block_number = self.chain[-1].index
        timestamp = block.timestamp
        transactions = block.transactions
        previous_hash = block.previous_hash
        nonce = block.nonce
        block_hash = block.hash

        max_length = max(
            len("Block #" + str(block_number)),
            len("Timestamp: " + str(timestamp)),
            len("Previous hash: " + str(previous_hash)),
            len("Nonce: " + str(nonce)),
            len("Hash: " + str(block_hash))
        )

        if block_number > 0:
            ## sleep for 0.5 seconds
            time.sleep(0.5)
            print("                                   |")
            time.sleep(0.5)
            print("                                   |")

            
        # Délimiteur supérieur du bloc
        print("―" * (max_length + 4))

        # Informations du bloc
        print("| Block #", block_number)
        print("| Timestamp: ", timestamp)
        print("| Transactions:")

        # Détails des transactions
        for transaction in transactions:
            print("|  Sender: ", transaction.sender)
            print("|  Recipient: ", transaction.recipient)
            print("|  Amount: ", transaction.amount)
            print("|  Signature: ", transaction.signature)

        # Autres informations du bloc
        print("| Previous hash: ", previous_hash)
        print("| Nonce: ", nonce)
        print("| Hash: ", block_hash)

        # Délimiteur inférieur du bloc
        print("―" * (max_length + 4))
        time.sleep(0.5)
        print("                                   |")
        time.sleep(0.5)
        print("                                   |")



