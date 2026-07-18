# methods of sets 
#1. joining sets using union
s1={1,2,5,8,12,42,11}
s2={4,6,2,5,8,90,123,32,43,54}
s3 = s1.union(s2)
print(s3)
#intersection in sets to find repeating numbers.
s1={1,2,5,8,12,42}
s2={4,6,2,5,8,90,123}
s3 = s1.intersection(s2)
print(s3)
#update function
s1.update(s2)
print(s1,s2)
s2.update(s1)
print(s1,s2)
if (s1==s2):
    print("yes")
else:
    print("no")
#symmetric_difference shows what is unique in both sets and exculdes repeatings completely.you can also update this
s4 = {'hanzala','ammar','ayan','affan'}
s5 = {'mustufa','umar','usman','hanzala'}
s6 = s4.symmetric_difference(s5)
print(s6)
# difference
s4 = {'hanzala','ammar','ayan','affan'}
s5 = {'mustufa','umar','usman','hanzala'}
s6 = s4.difference(s5)
print(s6)
#isdisjoint (checks if items of given set are visting other sets they are not able to perform union intersection.2 sets are disjointed when 
# they have no element in common),mostly used to check if 2 sets have common items in them.
# for example 
set1={12,14,2,3,4} #no common items prints true
set2={13,15,6,7,6}
print(set1.isdisjoint(set2))
# issuperset checks if original set has items of certain set for a super set items must be same though not all items are there 
#only items that match org set must be present with no other items.
cities={"tokyo","seoul","karachi","berlin","moscow"}
cities2={"seoul","delhi","balochistan","bangkok"}
print(cities.issuperset(cities2))
cities3={"tokyo","seoul","karachi","berlin","moscow",}
print(cities.issuperset(cities3))
# subsets are near same as supersets checking if one set has elemnts of org set.
print(cities3.issubset(cities))
# add method used to add items to sets only 1 element may be added at a time.
cities.add("helsinki")
print(cities)
#remove\discard methods.remove again only takes 1 item at a time.main diff bw remove and discard is that when you try to remove an item
#thats not present in a set remove gives error while discard does not.
set1={1,2,3,4,5,6,7,8,9,10}
print(set1)
set1.remove(3)
print (set1)
#discard
set1={1,2,3,4,5,6,7,8,9,10}
print(set1)
set1.discard(32) #gives no error even when 32 is notpresent in set remove would give type error if used here.
print (set1)
#pop removes the last item of the set but since sets are random we dont know which item will get removed but we can accesss it.
numbers={1,2,3,4,5,6,7,8}
items= (numbers.pop())
print(numbers)
print(items)
#del is not a method!!!, it is a keyword used to delete sets completely
even_numbers={2,4,6,8,10,12,14}
del even_numbers
# print(even_numbers)#gives error since set doesnt exist
# clear is used if we want to delete all items in a set but not the set itself.
odd_numbers={1,3,5,7,9,11}
print(odd_numbers)
odd_numbers.clear()
print(odd_numbers)




