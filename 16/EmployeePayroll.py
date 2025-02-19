class Employee:
    def __init__(self,employeeID,name,hourlyRate) -> None:
        self.employeeID = employeeID
        self.name = name
        self.hourlyRate = hourlyRate
    
    def calculatePay(self,hoursWorked):
    
        cal=self.hourlyRate*hoursWorked
        return cal
        

class Payroll:
    def __init__(self,employees) -> None:
        self.employees = employees

    def processPayroll(self,hoursMap):
        payroll_map={}
        for i in self.employees:
            if i.employeeID in hoursMap:
                payroll_map[i.employeeID] = i.calculatePay(hoursMap[i.employeeID])

        return payroll_map