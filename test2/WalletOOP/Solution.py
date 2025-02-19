class Transaction:
    def __init__(self,type,amount,fee):
        self.type=type
        self.amount=amount
        self.fee=fee
    def __str__(self):
        pass

class Wallet:
    def constracter(self,withdrawalLimit,withdrawalFeePercentage):
        
        
        self.withdrawalLimit= withdrawalLimit
        self.withdrawalFeePercentage=withdrawalFeePercentage


        self.balance=0.0
        self.tansaction=[]

        print(f"Wallet initialized with withdrawalLimit: {self.withdrawalLimit} , withdrawalFeePercentage: {withdrawalFeePercentage}")
       
    def deposit(self,amount):
        
        if amount <= 0:
            print(f"Deposit of {amount} failed. Balance remains: {self.balance}")
        else:
            self.balance+=amount
            transaction = Transaction("DEPOSIT", amount, 0.0)####gpt
            self.tansaction.append(amount)

        
            print(f"Deposit of {amount}successful. Current balance: {self.balance}")
        
    def withdraw(self,amount,fee):
        # self.balance-=amount
        
        if amount<=0 or amount>self.balance or amount> self.withdrawalLimit:
            print(f"Withdrawal of {amount} failed. Balance remains: {self.balance}")
        else:
            self.balance-=amount

            print(f"Withdrawal of {amount} successful with a fee of {self.fee}. Current balance: {self.balance}")
        
    def getBalance(self):
        print(f"Current Balance: {self.balance}")        
    def getTransactions(self):
        print("Transaction History:")
        if self.getTransactions:
            print(f"[{', '.join(self.getTransactions)}]")
        else:
            print([])


    def run_wallet(self):
        while True:
            try:
                s=input().split(" ")
                # print(s[1])
                # print(s[0])
                print(s)
                
                
                if len(s)==2:
                    
                    
                    withdrawalLimit=s[0]
                    withdrawalFeePercentage=s[1]
                    self.constracter(withdrawalLimit,withdrawalFeePercentage)
                    
                #   print(s[0])   
                elif s[0]== 'deposit':
                    amount=float(s[1])
                    print(amount)
                    print(s[1])
                    print(s[0])
                    self.deposit(amount)
                elif s[0]=="withdraw":
                    amount=float(s[1])
                    self.withdraw(amount)
                elif s[0]=="getBalance":
                    self.getBalance()
                elif s[0]=="getTransactions":
                    self.getTransactions()
                else:
                    break

                    
                  
            except:
                break
if __name__=="__main__":
    wallet=Wallet()
    wallet.run_wallet()
# try:
#     fun=Wallet()
#     while(True):
#         s=input().split(" ")
#         # print(s)
#         if len(s)==2:
#             withdrawalLimit=s[0].strip(",")
#             withdrawalFeePercentage=s[1].strip(",")
#             # print(s[1])
#             # print(s[0])
#             # fun.constracter(withdrawalLimit,withdrawalFeePercentage)
#         elif s[0] == "deposit":
#             print(s)
#             amount=float(s[1].strip(","))
#             print(s[1])
#             fun.deposit(amount)
#         elif s[0]=="withdraw":
#             amount=float(s[1].strip(","))
#             fun.withdraw(amount)
#         elif s[0]=="getBalance":
#            fun.getBalance()
#         elif s[0]=="getTransactions":
#             fun.getTransactions()

# except EOFError:
#     pass