import time


def startUI():
    print("\n                 Starting blockchain UI...")
    print("-----------------------------------------------------------\n")

def printBlock(block) -> None:
    block_number = block.index
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

    if len(transactions) == 0:
        print("|        No transactions")
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