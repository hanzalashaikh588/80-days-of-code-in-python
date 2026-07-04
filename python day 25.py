#manipulating Tuples.
countries=('germany','brazil','spain','argentina','portugal','pakistan','india')
temp=list(countries)#convert list to Tuples
temp.append('russia') #add items 
temp.pop(6) #remove items
temp[0]= 'croatia' #change items
temp.sort() #if some ietsm are lowercase and uppercase .sort doesnt function use temp.sort(key=str.lower)
countries=tuple(temp) #reverse list back to tuple
print(countries)
#merge 2 tuples to create a 3rd tuple.
even=(1,2,4,6,8,10)
odd=(1,3,5,7,9,11)
both = even + odd
print(both)
#tuple methods
tuple1=(0,1,2,3,4,5,2,3,4,5,0,1,1)
f=tuple1.count(1)
# index\ranges
tuple2=(1,2,4,5,7,7,8,9,7,6)
q=tuple2.index(7)
print('index of 7 in tuple2 is:' , q)
q=tuple2.index(7 , 6 , 9)
print('index of 7 in tuple2 in certain range is:' , q)


