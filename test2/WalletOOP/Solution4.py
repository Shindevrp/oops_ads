    class Transaction:
    def __init__(self, type, amount, fee):
        self.type = type
        self.amount = amount
        self.fee = fee

    def __str__(self):
        # String representation of the transaction (for easier printing)
        return f"{self.type} {self.amount} (Fee: {self.fee})"

class Wallet:
    def __init__(self, withdrawalLimit, withdrawalFeePercentage):
        # Corrected constructor method name: __init__
        self.withdrawalLimit = withdrawalLimit
        self.withdrawalFeePercentage = withdrawalFeePercentage

        self.balance = 0.0
        self.transactions = []  # Fixed typo from 'tansaction' to 'transactions'

        print(f"Wallet initialized with withdrawalLimit: {self.withdrawalLimit}, withdrawalFeePercentage: {self.withdrawalFeePercentage}%")
       
    def deposit(self, amount):
        if amount <= 0:
            print(f"Deposit of {amount} failed. Balance remains: {self.balance}")
        else:
            self.balance += amount
            # Create a deposit transaction with 0 fee
            transaction = Transaction("DEPOSIT", amount, 0.0)
            self.transactions.append(transaction)  # Corrected to append the transaction object

            print(f"Deposit of {amount} successful. Current balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance or amount > self.withdrawalLimit:
            print(f"Withdrawal of {amount} failed. Balance remains: {self.balance}")
        else:
            # Calculate fee
            fee = amount * (self.withdrawalFeePercentage / 100)
            total_amount = amount + fee

            if total_amount > self.balance:
                print(f"Withdrawal of {amount} failed. Balance remains: {self.balance}")
            else:
                self.balance -= total_amount
                # Create a withdrawal transaction with calculated fee
                transaction = Transaction("WITHDRAW", amount, fee)
                self.transactions.append(transaction)  # Corrected to append the transaction object

                print(f"Withdrawal of {amount} successful with a fee of {fee}. Current balance: {self.balance}")
        
    def getBalance(self):
        print(f"Current Balance: {self.balance}")
        
    def getTransactions(self):
        print("Transaction History:")
        if self.transactions:
            for idx, transaction in enumerate(self.transactions, 1):
                print(f"{idx}. {transaction}")  # This will call __str__ from the Transaction class
        else:
            print("[]")
    
    def run_wallet(self):
        while True:
            try:
                s = input().split(" ")
                
                if len(s) == 2:
                    # Handling withdrawalLimit and withdrawalFeePercentage initialization
                    withdrawalLimit = float(s[0])
                    withdrawalFeePercentage = float(s[1])
                    self.__init__(withdrawalLimit, withdrawalFeePercentage)  # Reinitialize wallet with the new values
                    
                elif s[0] == 'deposit':
                    amount = float(s[1])
                    self.deposit(amount)
                
                elif s[0] == "withdraw":
                    amount = float(s[1])
                    self.withdraw(amount)
                
                elif s[0] == "getBalance":
                    self.getBalance()
                
                elif s[0] == "getTransactions":
                    self.getTransactions()
                
                else:
                    break
                    
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    wallet = Wallet(0.0,0.0)  # Initial example wallet values
    wallet.run_wallet()
