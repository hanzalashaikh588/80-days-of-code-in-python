# dictionaries in python
dic={ 'earth': "planet in solar system" , 
'book': "object used to store/gather information"}
print(dic['earth'])
print(dic['book'])
#example 2
employees={365 : 'harry' ,
457 : 'fatima' , 234 : 'ayan' }
print(employees[365])
#example3
info={'name': 'hassan' , 'age' : 19 , 'eligible' : True}
print(info)
#print(info['name2']) #throws error in program
print(info.get('name2')) #does not throw error
# accessing multiple values
print(info)
print(info.keys()) 
print(info.values())
# using for loop
for key in info.keys():
    print(info[key])
#usinf f strings
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
# .items to access key value pairs
print(dic.items())
for key, value in dic.items():
    print(f"the value corresponding to the key {key} is {value}")
