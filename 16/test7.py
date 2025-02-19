from EmployeePayroll import Employee,Payroll
def main():
# Create employees
    emp1 = Employee(1, "Alice", 20.0)
    emp2 = Employee(2, "Bob", 25.0)
    emp3 = Employee(3, "Charlie", 30.0)
    payroll = Payroll([emp1, emp2, emp3])
    # Hours mapping including an edge case with zero hours
    hours_map = {1: 40.0, 2: 35.0, 3: 0.0}
    pay_results = payroll.processPayroll(hours_map)
    print("Payroll results:")
    for emp_id, pay in pay_results.items():
        print(f"Employee ID {emp_id} earned: {pay}")
if __name__ == '__main__':
    main()