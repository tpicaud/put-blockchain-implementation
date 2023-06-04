### **Group : Lima**
<br>

# Getting started  
## Introduction
The application is a basic implementation of a blockchain that you can run locally on your computer. The goal of this blockchain is to store transactions between addresses. In order to interact with it there is also a wallet application that allows you to create key pair, see your balance and send transaction.

## 1. Setup the environment
You have 2 options:
- install python packages specified in `requirements.txt` on your machine.

OR

- Setup virtual environment with venv : ```python3 -m venv <env_name>```
- install packages : ```pip install -r requirements.txt```

## 2. Run the blockchain

Simply run ```python3 blockchain/main.py``` in a separate terminal.

## 3. Run the wallet

Simply run ```python3 wallet/main.py``` in a separate terminal. The wallet provides a CLI that you can use to interact with the blockchain. The commands are the following :
- ```help```
    See commands
- ```create```  
    Create a new wallet
- ```balance <address>```  
    Get balance of an address (where ```<address>``` is optional)
- ```send <amount> <address>```  
    Send a transaction
- ```exit```

### ***Important note: each account has a base amount of 5 coins***

## 4. Additional information

- Valid addresses are only 64 hex characters
- Wallet key-pair is lost when exiting the application
- For testing, create two or more wallets in separated terminals and send coins between their addresses