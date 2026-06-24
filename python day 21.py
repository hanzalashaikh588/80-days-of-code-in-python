#default arguments
def average(a=4,b=5,c=9):
    print("the average is ", (a+b+c)/2)
average()
#or 
def average(a=4,b=5,c=4):
    print("the average is ", (a+b+c)/2)
average(b=10)
#keyword arguments(order may be changed upon need)
average(b=6,c=5,a=13)
#required arguments ( essenitally if default arguments are not provided we must give them values when calling the argument or we get errors.)
def name(fname, mname, lname):
    print("hello", fname, mname , lname)
name("charles","oliviera,","junior")
# variable-length arguments , having 2 types 
def Average(*numbers):
   # print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("the Average is", sum/len(numbers))
Average(5 ,6, 7)
#return fucntions
def Average(*numbers):
   # print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c = Average(50 ,63, 71)
print(c)
#example of why return statements are used in programs.
if (c<0):
     print("you failed the test")
else:
    print("you passed the test")


    
