#list methods
#1. .append (adds things to list)
l =[1, 2, 3, 4, 5,1,1]
print(l)
l.append(7)
print(l)
#.sort() 
k =[13, 56, 25, 2, 3, 4, 5, 1]
print(k)
k.sort() # remeber to leave empty brackets!!!
print(k)
# it can also be reversed
k.sort(reverse=True)
print(k)
#index 
print(l.index(1))
#count
print(l.count(1))
#insert to add items to list in given index 
k.insert(3,432)
print(k)
#extend
h=[1223,124,165]
# l.extend(h)
# print(l)
#concetanating lists
x=k+h+l
print(x)
#.pop removes and returns the last element of the list
numbers=[10,20,30,40]
val=numbers.pop()
print(val)
data=[1,2,3]
data.clear()
print(data)