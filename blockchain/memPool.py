from transaction import Transaction


class MemPool:
    def __init__(self) -> None:
        self.pending_transactions = []
        
    def addTransaction(self, transaction: Transaction) -> None:
        ## Check if the mempool is full
        if len(self.pending_transactions) < 10000:
            ## Add a transaction to the mempool
            self.pending_transactions.append(transaction)

    def getTransactions(self) -> list:
        ## Return the list of transactions in the mempool
        return self.pending_transactions
    
    def removeTransactions(self, transactions: list) -> None:
        ## Remove the list of transactions from the mempool
        for transaction in transactions:
            self.pending_transactions.remove(transaction)