#local vs global variables
x = 10  # global variable
print(x)
def function_hello():
    y = 5 # local variable exists only inside this function
    global x
    x = 12 # also a global variabe if we print x outside the func we will get 10
    print(x)
    print(y)
function_hello()
# print(y)  this gives us an error since y only exists in hello function 
         #but if we print (x) which is a global variable we get no error
print(x)
