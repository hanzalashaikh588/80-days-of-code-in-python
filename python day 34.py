# dictionary methods
#update method
class1a={125 : 20 , 127 : 87 , 162 : 92}
class1b={123 : 45 , 129 : 66 , 124 : 98}
print(class1a)
class1a.update(class1b)
print(class1a)
# clear method
employees={'ali' :2020 , 'hussain' : 2019 , 'hammad' : 2016 }
employees.clear()
print(employees)
groceries={'onion' : '1kg' , 'potato' : '2kg' , 'tomato' : '1kg' , 'carrot' : '0.5kg'}
print(groceries)
groceries.pop('onion')
print(groceries)
# pop item removes last key value pair from dict
groceries.popitem()
print(groceries)
dictionary={123 :124 , 124 :54 , 12:67}
# del method
#del dictionary will delete the entire dictionary if key value pair is not provided
print(dictionary)
del dictionary[123]
print(dictionary)
