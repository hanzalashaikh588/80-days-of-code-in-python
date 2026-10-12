# inheritance in python
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"The name of the employee is: {self.name} and his id is: {self.id}")

class programmer(Employee):
    def showlanguage(self):
        print("The preferred language is python")


a = Employee("kashif", 9987)
a.showdetails()
a2 = programmer("harry", 9988)
a2.showdetails()
a2.showlanguage()

#example
class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def Sgrades(self):
        print(f"The grade of student {self.name} is {self.grade} in physics")

class subject(student):
    def showsubject(self):
        print(f"The grade of student {self.name} is {self.grade} in maths")


s1 = subject("ayan", "A+")
s1.Sgrades()
s1.showsubject()
s2 = subject("hasnain", "B-")
s2.Sgrades()
s2.showsubject()
s3 = subject("ammar", "F")
s3.Sgrades()
s3.showsubject()
s4 = subject("aslam", "C+")
s4.Sgrades()
s4.showsubject()


