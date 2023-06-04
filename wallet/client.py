from cli import Cli
from wallet import Wallet
from colorama import Fore, Style



class Client:
    def __init__(self):
        self.wallet = None
        self.cli = Cli(self)

    def createWallet(self):
        self.wallet = Wallet()
        print("Generating key pair...")
        self.wallet.generate_key_pair()
        print(Fore.GREEN+"Key pair generated successfully!"+Fore.RESET)
        print("Public key: " + Style.BRIGHT + Fore.CYAN + self.wallet.get_public_key_hex()
              +Style.RESET_ALL + Fore.RESET)

    def sendTransaction(self, recipient_address: str, amount: float):
        if self.wallet is None:
            print("You must create a wallet first.")
            return
        else:
            if len(recipient_address) == 64:
                self.wallet.send_transaction(recipient_address, amount)
            else:
                print("Invalid address.")
                return

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
        
