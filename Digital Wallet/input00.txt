class EWallet:
    def __init__(self):
        self.funds = 0.0
        self.transactions = []

    def reset_wallet(self):
        self.funds = 0.0
        self.transactions = []
        print("Wallet reset with balance 0 and empty transaction history.")

    def show_balance(self):
        print(f"Current balance: {self.funds:.1f}")

    def deposit_funds(self, input_line):
        try:
            amount = float(input_line.split('=')[1].strip())
            if amount > 0:
                self.funds += amount
                self.transactions.append("+" + str(round(amount, 1)))
                print(f"Balance updated to {self.funds:.1f}, transaction history logged.")
            else:
                print("Invalid amount. Transaction not recorded.")
        except Exception as e:
            print(f"Error in deposit_funds: {e}")

    def process_payment(self, input_line):
        try:
            amount = float(input_line.split('=')[1].strip())
            if amount > 0 and self.funds >= amount:
                self.funds -= amount
                formatted_amount = f"{round(amount, 2):.2f}" if amount % 1 != 0 else f"{round(amount, 1):.1f}"
                self.transactions.append(f"-{formatted_amount}")
                print(f"Balance updated to {self.funds:.1f}, transaction history logged.")
            elif amount <= 0:
                print("Invalid amount. Transaction not recorded.")
            else:
                print("Insufficient balance. Transaction not recorded.")
        except Exception as e:
            print(f"Error in process_payment: {e}")

    def list_transactions(self):
        if self.transactions:
            print(f"[{', '.join(self.transactions)}]")
        else:
            print([])

    def execute_wallet_operations(self):
        while True:
            try:
                line = input().strip()
                if line == "STOP":
                    break

                if line.startswith("Method:"):
                    method_name = line.split(":")[1].strip()
                    inputs_line = input().strip()
                    if method_name == "reset_wallet":
                        self.reset_wallet()
                    elif method_name == "deposit_funds":
                        self.deposit_funds(inputs_line)
                    elif method_name == "process_payment":
                        self.process_payment(inputs_line)
                    elif method_name == "list_transactions":
                        self.list_transactions()
                    elif method_name == "show_balance":
                        self.show_balance()
                    else:
                        print("Invalid method name.")
                else:
                    print("Invalid input format. Please start with 'Method:'.")
            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    wallet = EWallet()
    wallet.execute_wallet_operations()
