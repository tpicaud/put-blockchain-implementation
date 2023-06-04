import datetime
import threading
import time
from typing import List
from block import Block
from memPool import MemPool
from transaction import Transaction
from blockchainUI import startUI, printBlock
from controller import Controller

class Blockchain:
    def __init__(self, chain: List[Block], difficulty: int, mem_pool: MemPool) -> None:
        self.chain = chain
        self.difficulty = difficulty
        self.mem_pool = mem_pool

    def addBlock(self, transactions: List[Transaction]) -> List[Transaction]:
        transactions = transactions.copy()
        if len(self.chain) == 0:
            # Genesis block
            previous_hash = "0"
            block = Block(0, self.get_current_timestamp(), [], previous_hash)
        else:
            # New block
            previous_block = self.chain[-1]

            ## Remove invalid transactions
            valid_transactions = []
            for transaction in transactions:
                if transaction.isValid() and self.get_balance(transaction.sender) >= transaction.amount:
                    valid_transactions.append(transaction)
            
            ## Create new block
            block = Block(previous_block.index + 1, self.get_current_timestamp(), valid_transactions, previous_block.hash)
            block.mineBlock(self.difficulty)
        self.chain.append(block)
        return transactions

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
    
    def receiveTransaction(self, transaction: Transaction) -> None:
        self.mem_pool.addTransaction(transaction)
    
    def get_balance(self, address: str) -> float:
        balance = 5 # Initial balance to facilitate testing
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.sender == address:
                    balance -= transaction.amount
                elif transaction.recipient == address:
                    balance += transaction.amount
        return balance


    def start(self) -> None:

        ## Start controller in a separate thread
        controller = Controller(self)
        thread  = threading.Thread(target=controller.run)
        thread.start()
        time.sleep(1)

        ## Start blockchain
        startUI()
        while True:
            added_transactions = self.addBlock(self.mem_pool.getTransactions())
            self.mem_pool.removeTransactions(added_transactions)                
            printBlock(self.chain[-1])    