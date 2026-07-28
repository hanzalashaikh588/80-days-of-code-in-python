# a = int(input("enter any value between 5 and 9 : "))
# if(a<5 or a>9):
#     raise ValueError("value is not between 5 and 9")
# else:
#      print("value  is between 5 and 9")

#example
# input2=input("do you wish to import data? (yes/no) : ")
# if (input2=="yes"):
#     raise ImportError("The data center is not running info cannot be imported")
# else:
#     print("exiting")
#import information from data servers
#example2 
a= (2j+45j)
b= (3j+45j)
print(a)
print(b)
c= complex(input("enter any complex value ( use j for imaginary unit):"))
raise ValueError("value is not a complex number")
raise TypeError("value is not complex")
try:
    d=a+b+c
    print(d)
except Exception as e:
    print("error is ",e)





