class person:
    name = "harry"
    occupation = "teacher"
    salary = 400
    def info(self):
        print(f"{self.name} is a {self.occupation}")
# self is that object on which the method is called.
a = person()
a.name = "harry 2"
a.occupation  = "accountant"
b = person()
b.name = "nikita"
b.occupation = "manager"
c = person()
#print(a.name,a.occupation)
a.info()
b.info()
c.info()