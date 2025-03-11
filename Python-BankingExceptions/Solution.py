class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountException("Deposit amount cannot be negative.")
        self.balance += amount
        # return self.balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountException("Withdrawal amount cannot be negative.")
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds for withdrawal.")
        self.balance -= amount
        # return self.balance
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, recipient, amount):
        if amount < 0:
            raise NegativeAmountException("Cannot transfer a negative amount.")
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds for withdrawal.")
        self.withdraw(amount)
        recipient.deposit(amount)
    

class NegativeAmountException(Exception):
    def __init__(self, message):
        self.message =message
       


class InsufficientFundsException(Exception):
    def __init__(self, message):
        self.message =message

class InvalidAccountException(Exception):
    def __init__(self, message):

        self.message =message