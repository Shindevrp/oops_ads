class Account:
    def __init__(self,accountNumber,accountHolder,balance):
        self.account_number = accountNumber
        self.accountHolder = accountHolder
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount

    def getBalance(self):
        return self.balance

    def withdraw(self,amount):
        if self.balance > amount and amount > 0:
            self.balance-= amount
            return True
        return False

class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolder, balance, interst):
        super().__init__(accountNumber, accountHolder, balance)
        self.interst = interst
    
    def calculateInterest(self):
        intrest = self.balance*(self.interst)
        self.balance -=intrest 
        return intrest 

class CurrentAccount(Account):
    def __init__(self, accountNumber, accountHolder, balance, over_balance):
        super().__init__(accountNumber, accountHolder, balance)
        self.over = over_balance

    def withdraw(self, amount):
        if self.balance + self.over >= amount and amount > 0:
            self.balance-= amount
            return True
        return False