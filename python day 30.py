#Recursions
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
        
print(factorial(5))
print(5*(factorial(2)))
#fibonacci sequence 
#f(0)=0
# f(1)=1
# f(2)=f(1)+f(0)
# f(n)=f(n-1)+f(n-2)
# write a program to run the fibonacci sequence!.
def f(n):
    if n == 0:
        return 0 
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)



print("This is the fibonacci sequence.")
n = int(input("enter your number : "))
print(f(n))