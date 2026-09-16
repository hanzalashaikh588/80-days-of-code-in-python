#map,filter,reduce functions.
def cube(x):
    return x * x * x

l= [2,3,4,6,7,9,12,15]
# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)
newl = list(map(cube, l))
print(newl)
print (cube(2))
#filter
def filter_function(a):
    return a >= 4
    
newl2 = list(filter(filter_function, l))
print(newl2)
#example:
student_marks = [50,70,25,62,75,15,29]
def filter_function2(b):
    return b >= 33

newl3 = list(filter(filter_function2, student_marks))
print(newl3)
#lambda
newl = list(map(lambda x: x*x*x,l))
print(newl)
#reduce
from functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y,numbers)
print(sum)


