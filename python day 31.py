#Sets in python
set1={1,2,3,4,4,3}#sets do not repeat items and sets are immutable and order in sets is random.
print(set1)
#sets like lists can hold diff data types
set2={3,True,9.5,3,'ok'}
print(set2)
#set1.sort() # fucntion arguments are not applicable for sets.
#print(set1+set2)
setnone={}#because syntax of set and dict are same data type is shown as dict this is wrong way to make empty set
print(type(setnone))
print(type(set1))
set3= set()
print(type(set3))
for value in set1:
    print(value)