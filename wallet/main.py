from wallet import Wallet

def main():

    wallet = Wallet()
    wallet.generate_key_pair()
    wallet.send_transaction("recipient_address_1", 4)
    print("Public key :", wallet.public_key_hex)

if __name__ == "__main__":
    main()