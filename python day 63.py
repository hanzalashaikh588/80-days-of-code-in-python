#static methods.
# static methods are methods the belong to a class rather than an instance of a class
# they are used to create utility methods that dont need information of instance.
# it also shows that methods can be used without self.
class Math:
    @staticmethod
    def add(a,b):
        return a + b

result = Math.add(1,4)
print(result)
# normal method
class math2:
    def __init__(self,num):
        self.num = num

    def add_to_num(self,n):
        self.num = self.num + n

a = math2(10)
print(a.num)
a.add_to_num(20)
print(a.num)

#example
class library:
    @staticmethod
    def add_books(a,b):
        print(f"the books added are {a} and {b}")

    @staticmethod
    def total_books(count):
        print(f"the total number of books added are {count}")
    
library.add_books("harry potter", "game of thrones")
library.total_books(2)
