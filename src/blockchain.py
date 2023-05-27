import datetime
from typing import List
from src.block import Block
from transaction import Transaction

class Blockchain:
    def __init__(self, chain: List[Block], difficulty: int) -> None:
        self.chain = chain
        self.difficulty = difficulty


    def addBlock(self, transactions: List[Transaction]) :
        if len(self.chain) == 0:
            # Genesis block
            previous_hash = "0"
            block = Block(0,self.get_current_timestamp(), previous_hash)
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

    def get_current_timestamp() -> int:
        current_datetime = datetime.datetime.now()
        timestamp = int(current_datetime.timestamp())
        return timestamp