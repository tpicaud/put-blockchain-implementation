import re
import colorama

from colorama import Fore, Style

class Cli:
    def __init__(self, client):
        self.client = client
        self.startCLI()

    def createWallet(self):
        self.client.createWallet()

    def sendTransaction(self, recipient_address: str, amount: float):
        self.client.sendTransaction(recipient_address, amount)


    def startCLI(self):
        print("Starting client... \n")
        colorama.init()
        while True:
            command = input(Style.BRIGHT + Fore.GREEN + "Client#  " + Style.RESET_ALL + Fore.RESET)

            ## Parsing the input
            if command == "exit":
                break

            if command == "help":
                print("create                      -> Create a new wallet")
                print("send <amount> <address>     -> Send a transaction")
                print("balance <address>?          -> Get balance of an address (default: your address)")
                print("exit                        -> Exit the client")
                continue

            ## Get balance
            match = re.match(r'balance(?: (.+))?', command)
            if match:
                parametre = match.group(1)
                if parametre:
                    self.client.getBalance(parametre)
                else:
                    self.client.getBalance()
                continue

            ## Create a new wallet
            match = re.match(r'create', command)
            if match:
                self.createWallet()
                continue

            ## Send a transaction
            match = re.match(r'send ([0-9]+(?:\.[0-9]+)?) (.+)', command)
            if match:
                amount = float(match.group(1))
                recipient_address = match.group(2)
                self.sendTransaction(recipient_address, amount)
                continue
             
            print("Invalid command.")
        
        colorama.deinit()