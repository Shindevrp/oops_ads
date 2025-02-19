from bankCustomer import BankAccount,Customer
def main():
    # Create a BankAccount and test deposit/withdrawal
    account = BankAccount("ACC001", 1000.0, "savings")
    
    account.deposit(500.0)
    if account.getBalance() != 1500.0:
        print("Error: Incorrect balance after deposit.")
    
    # Test valid withdrawal
    success_withdraw = account.withdraw(300.0)
    print("Withdrawal of 300 successful:", success_withdraw)
    
    # Test invalid withdrawal (exceeding balance)
    fail_withdraw = account.withdraw(2000.0)
    print("Withdrawal of 2000 (should fail):", fail_withdraw)
    
    # Create a Customer and add the account
    customer = Customer(1, "John Doe", [])
    customer.addAccount(account)
    
    retrieved = customer.getAccount("ACC001")
    print("Retrieved account balance:", retrieved.getBalance())
    
    # Test retrieval of a non-existing account
    non_exist = customer.getAccount("ACC999")
    print("Non-existent account retrieval:", non_exist is None)

if __name__ == '__main__':
    main()
