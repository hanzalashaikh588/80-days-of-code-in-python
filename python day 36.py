# exception handling
a = input(("Enter your number : "))
print(f"Multiplication table of {a} is :")
try:
    for i in range(1,11):
        print(f"{int(a)} X {(i)} = {int(a)*i}")
except:
    print("some error has occured")

print('some imp lines of code')
print('end of program')
# handling specific errors
try:
    num = int(input("Enter an integer : "))
    print(f"{num} is an integer")
except ValueError:
    print("number entered is not an integer")
#example of another error.
def function_age_calculator():
    name=input("enter your name : ")
    try:
        age=int(input("enter your age:"))
        age1==age
    except ValueError:
        print("please enter numbers ")
    return
    agenxtyr=(1 + age1)
    print(f"your age next year will be {agenxtyr} ")
function_age_calculator()


    


