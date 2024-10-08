from SavingsAccount import SavingsAccount
import hashlib  

class AccountManager:
    def __init__(self):
        self.accounts = {} 
        self.credentials = {}

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def create_account(self, account_type, account_number, holder_name, balance=0.0, username=None, password=None, pin=None):
        if account_type == "savings":
            account = SavingsAccount(account_number, holder_name, balance)
            self.accounts[account_number] = account
            self.credentials[username] = {
                "password": self.hash_password(password),
                "pin": pin,
                "account_number": account_number
            }
            return account

    def verify_login(self, username, password): #For veryfing username and password
        
        if username in self.credentials and self.hash_password(password) == self.credentials[username]["password"]:
            return self.credentials[username]["account_number"]
        return None

    def verify_pin(self, username, pin): #verified Secret Pin
        if username in self.credentials:
            return self.credentials[username]["pin"] == pin
        return False

    def change_password(self, username, new_password): #changing password
        if username in self.credentials:
            self.credentials[username]["password"] = self.hash_password(new_password)

    def change_pin(self, username, new_pin): #change PIN
        if username in self.credentials:
            self.credentials[username]["pin"] = new_pin
