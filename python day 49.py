# file io in python
#r means opening file in read mode
#w opens the file for writing only or makes one if file doesnt exist
#a append mode can be used to add things to the end of the file and also creates file if it doesnt exist
#x creates a file gives error if file alr exists
#t t module is used to handle txt files
#b used to handle binary files example pdfs, images, jpg etc
# READING A FILE
# f = open('myfile.txt' , 'r')
# text = f.read()
# print(text)
# f.close() 
# WRITING A FILE
# f = open('myfile.txt' , 'w')
# f.write("hello world")
# f.close()
# f = open('myfile.txt' , 'a')
# f.write("hello world")
# f.close()
#WITH STATEMENT
with open('myfile.txt' , 'a')as f:
    f.write("hey i am inside the house")