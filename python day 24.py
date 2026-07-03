#Tuples , tuples are immutable.
tup=(95,65,45,'book',True)
print(type(tup))
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
#print(tup[21]) out of range index error
print(len(tup))
#tuples are like lists but are immutable apart from that almost all is the same.
#negative indexing
print(tup[-2]) 
#items check
if 65 in tup:
    print('65 is present in the tuple')
else:print('not present in tuple')
#range of index
countries=('germany','brazil','spain','argentina','portugal')
print(countries[:3])
#printing specific items.
animals=('cow','lion','zebra','cat','dog','hipppo','leopard','goat','eagle','tiger')
print(animals[0:10:3])



