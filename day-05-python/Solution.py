class Account:
    def __init__(self,accountNumber,accountHolder,balance):
        self.accountNumber = accountNumber
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
class LoanAccount(Account):
    def __init__(self, accountNumber, accountHolder, loanAmount, interestRate):
        # super().__init__(accountNumber, accountHolder, balance)
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.loanAmount = loanAmount
        self.interestRate = interestRate
    
    def repay(self,amount):
        if amount > 0 and amount <= self.loanAmount:
            self.loanAmount -= amount
    def calculateInterest(self):
        intrest = self.loanAmount * (self.interestRate)
       
        return intrest 
    
    def getOutstandingLoan(self):
        return self.loanAmount
    
class Transaction:
    def __init__(self, transactionID,accountNumber,type , amount, transcationDate):
        # super().__init__(accountNumber, accountHolder, balance)
    
        self.transactionID = transactionID
        self.accountNumber = accountNumber
        self.type = type
        self.amount = amount
        self.transactionDate = transcationDate
    def __str__(self) -> str:
        
        return f"{self.transactionDate} - {self.type} of {self.amount} on Account {self.accountNumber}"

class Person:
    def __init__(self, personID, name):
        self.personID = personID
        self.name = name
        self.accounts = []
        self.relationships = []
    
    def addAccount(self, account):
        self.accounts.append(account)
    
    def addRelationship(self, person):
        self.relationships.append(person)
    def getAccounts(self):  
        return self.accounts




class Bank:
    def __init__(self) -> None:
        self.accounts = []

    def addAccount(self, account):
        self.accounts.append(account)

    def findAccount(self, accountNumber):
        for account in self.accounts:
            if account.accountNumber == accountNumber:
                return account
        
    def transfer(self, fromAccountNumber, toAccountNumber, amount):
        fromAcc = self.findAccount(fromAccountNumber)
        toAcc = self.findAccount(toAccountNumber)
        
        if fromAcc.withdraw(amount):
            toAcc.deposit(amount)
            return True
        
        return False