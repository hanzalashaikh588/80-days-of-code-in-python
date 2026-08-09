#seek() fucntion
# with open('file.txt','r'):
#     print(type(f))
#     # move to the 10th byte in the file
#     f.seek(10)
#     # read the next 5 bytes
#     data = f.read(5)
#     print(data)
# truncate() function
with open('sample.txt','w')as f:
    f.write("hello world")
    f.truncate(5)
with open('sample.txt','r')as f:
    print(f.read())

