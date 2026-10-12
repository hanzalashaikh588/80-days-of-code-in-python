class person(): # parameterized constructors
    def __init__(self , name , occ):
        print("hey i am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("harry","developer")
b = person("nikita" , "accountant")
a.info()
b.info()

#example:default constructor.
class details():
    def __init__(self):
        print("a dolphin is a mammal.")
obj1=details()
