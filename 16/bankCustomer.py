class BankAccount:
    def __init__(self,accountNumber,balance,accountType) -> None:
        self.accountNumber = accountNumber
        self.balance=balance
        self.accountType=[]

    def deposit(self,amount):
        if amount<=0:
            return False
        else:
            self.balance+=float(amount)
            return True
        
    def withdraw(self,amount):
        if self.balance<amount:
            return False
        self.balance-=float(amount)
        return True
        
    def getBalance(self):
        return self.balance
        

class Customer:
    def __init__(self,customerID,name,accounts) -> None:
        self.customerID = customerID
        self.name = name
        self.accounts = accounts

    def addAccount(self,BankAccount):
        self.accounts.append(BankAccount)

    def getAccount(self,accountNumber):
        for BankAccount in self.accounts:
            # print("fghj1")
            if BankAccount.accountNumber==accountNumber:
                # print("ghjk2")
                return BankAccount
        return None
