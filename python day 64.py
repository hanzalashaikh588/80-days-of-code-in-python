#instance vs class variables
#instance variables are checked first if not found class variables are used.
class Employee:
    company_name = "Apple" #class variable
    def __init__(self,name):
        self.name = name
        self.raise_amount = 100
    def showdetails(self):
        print(
            f"The name of the employee is {self.name} and the raise amount is {self.raise_amount} "
            f"\n the company name is {self.company_name} "
        )
        
emp1 = Employee("Harry")
emp1.showdetails()
emp2 = Employee("ayan")
emp2.raise_amount = 90 #instance variable
emp2.showdetails()
Employee.company_name = "microsoft" #instance variable
emp3 = Employee("ammar")
emp4 = Employee("hanzala")
emp3.showdetails()
emp4.showdetails()