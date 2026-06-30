#lists
marks= [ 3, 7, 10,'String', True, 68,23,34,56,12,14]
#index  [0][1][2] etc.
#in lists there can be a mix of multiple different data types,list index starts from [0].
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# to check wether an item is present in a list works with strings as well.
if 8 in marks:
   print("yes")
else:
   print("no")
# jump index
print(marks)
print(marks[1:8]) # string slicing
# in [0:2]0 is the start but 2 will not be printed only 0 to 1,  including 2 and upwards nothing will be printed.
print(marks[1:8:3])
#list comprehenison
lst = [i*i for i in range(20)]
print(lst)
lst= [i*i for i in range(20) if i%2==0]
print(lst)
print(len(lst))
lst = [i*i for i in range(-5)]  # Generates [0, 1, 4, 9, 16]