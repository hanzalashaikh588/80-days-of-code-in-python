#class methods in python.
class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
    
    @classmethod
    def Change_company(cls , new_company):
        cls.company = new_company

e1 = Employee()
e1.name = "harry"
e1.show()
e1.Change_company("Tesla")
e1.show()
print(Employee.company)