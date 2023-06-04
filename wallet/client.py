from cli import Cli
from wallet import Wallet


class Client:
    def __init__(self):
        self.wallet = None
        self.cli = Cli(self)

    def createWallet(self):
        self.wallet = Wallet()
        self.wallet.generate_key_pair()

    def sendTransaction(self, recipient_address: str, amount: float):
        if self.wallet is None:
            print("You must create a wallet first.")
            return
        else:
            self.wallet.send_transaction(recipient_address, amount)

    def getBalance(self, address: str = None):
        if self.wallet is None:
            print("You must create a wallet first.")
            return
        else:
            if address is None:
                address = self.wallet.get_public_key_hex()
            print("Getting balance for address " + address + "...")
            balance = self.wallet.get_balance(address)
            print("Balance: " + str(balance))
        
