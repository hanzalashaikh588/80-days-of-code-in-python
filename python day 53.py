# is vs == in python
a = 4
b = "4"
print(a is b) # exact location of object in memory
print(a==b)   #value
#both are false here because of diff values and diff locations due to string and int difference
a = 3
b = 3
print(a is b)
print(a==b)
# here both are true since 3 here is int in both and is equal and stored in the same location.
a = [1,4]
b = [1,4]
print(a is b)
print(a==b)
#here is gives false because lists are mutable and hence have different locations in memory.
a = (2,5,7)
b = (2,5,7)
print(a is b)
print(a==b)
# both are true here because tuples are immutable hence stored in same location memory.
a = "france"
b = "france"
print(a is b)
print(a==b)
