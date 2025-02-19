class DigitalWallet:
    def __init__(self):
        self.balance = 0.0
        self.transaction_history = []

    def initialize_wallet(self):
        print("Wallet initialized with balance 0 and empty transaction history.")

    def display_balance(self):
        print(f"Current balance: {self.balance:.1f}")

    def add_funds(self, input):

        amount = float(input.split('=')[1].strip())
        if amount > 0:
            self.balance += amount
            self.transaction_history.append("+" + str(round(amount, 1)))
            print(f"Balance updated to {self.balance:.1f}, transaction history logged.")
        else:
            print("Invalid amount. Transaction not recorded.")
            
        

    def make_payment(self, input):
        amount = float(input.split('=')[1].strip())
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
                
            self.transaction_history.append(f"-{amount}")
            print(f"Balance updated to {self.balance:.1f}, transaction history logged.")
        elif amount <= 0:
            print("Invalid amount. Transaction not recorded.")
        else:
            print("Insufficient balance. Transaction not recorded.")
        

       

    def view_transaction_history(self):
        print(f"[{', '.join(self.transaction_history)}]")
       
    def run_wallet_operations(self):
        while True:
            try:
                s= input().strip()  
                if s == " ":
                    break

                if s.startswith("Method:"):
                    method_name = s.split(":")[1].strip()
                    inputs = input().strip()  
                    if method_name == "initialize_wallet":
                        self.initialize_wallet()
                    elif method_name == "add_funds":
                        self.add_funds(inputs)
                    elif method_name == "make_payment":
                        self.make_payment(inputs)
                    elif method_name == "view_transaction_history":
                        self.view_transaction_history()
                    elif method_name == "display_balance":
                        self.display_balance()
                    else:
                        print("Invalid method name.")
                else:
                    print("Invalid input format. Please start with 'Method:'.")
            except EOFError:
                
                break
            except Exception as e:
                print(f"Error: {e}")



if __name__ == "__main__":
    wallet = DigitalWallet()
    wallet.run_wallet_operations()
