from account_manager import AccountManager

def show_menu():
    print("\n--- Main Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Change Password")
    print("6. Change PIN")
    print("7. Logout")

def register_new_user(manager):
    print("\n--- New Customer Registration ---")
    holder_name = input("Enter your name: ")
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    pin = input("Set a 4-digit secret PIN for transactions: ")

    account_number = int(input("Enter a new account number: "))
    balance = float(input("Enter the initial balance: "))

    manager.create_account("savings", account_number, holder_name, balance, username, password, pin)
    print(f"Account created successfully for {holder_name} with account number {account_number}.")

def login(manager):
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    account_number = manager.verify_login(username, password)
    if account_number:
        print(f"Login successful. Welcome {username}!")
        return account_number, username
    else:
        print("Invalid username or password.")
        return None, None

def main():
    manager = AccountManager()

    print("\nWelcome to the Bank System")

    while True:
        action = input("\nAre you a new customer? (yes/no): ").lower()
        if action == "yes":
            register_new_user(manager)
        else:
            account_number, username = login(manager)
            if account_number:
                account = manager.accounts[account_number]

                while True:
                    show_menu()
                    choice = input("\nSelect an option: ")

                    if choice == '1':  # Check Balance
                        print(f"\nYour balance: {account.get_balance()}")

                    elif choice == '2':  # Deposit Money
                        pin = input("Enter your 4-digit PIN to proceed: ")
                        if manager.verify_pin(username, pin):
                            amount = float(input("Enter amount to deposit: "))
                            account.deposit(amount)
                            print(f"{amount} deposited successfully.")
                            print(f"New balance: {account.get_balance()}")
                        else:
                            print("Invalid PIN.")

                    elif choice == '3':  # Withdraw Money
                        pin = input("Enter your 4-digit PIN to proceed: ")
                        if manager.verify_pin(username, pin):
                            amount = float(input("Enter amount to withdraw: "))
                            if account.withdraw(amount):
                                print(f"{amount} withdrawn successfully.")
                            else:
                                print("Insufficient funds.")
                            print(f"New balance: {account.get_balance()}")
                        else:
                            print("Invalid PIN.")

                    elif choice == '4':  # View Transaction 
                        print("\nTransaction History:")
                        for transaction in account.get_transaction_history():
                            print(transaction)

                    elif choice == '5':  # Change Password
                        new_password = input("Enter your new password: ")
                        manager.change_password(username, new_password)
                        print("Password changed successfully.")

                    elif choice == '6':  # Change PIN
                        new_pin = input("Enter your new 4-digit PIN: ")
                        manager.change_pin(username, new_pin)
                        print("PIN changed successfully.")

                    elif choice == '7':  # Logout
                        print("You have logged out successfully.")
                        break

                    else:
                        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
