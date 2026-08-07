#file io methods in python
#1. readline() method
f = open('myfile.txt' , 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in math are : {m1*2}")
    print(f"Marks of student {i} in physics are : {m2*2}")
    print(f"Marks of student {i} in chemistry are : {m3*2}")
    print(line)
f.close()

#2 writeline() method
f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

f = open('myfile2.txt', 'w')
lines = ['line 1', 'line 2', 'line 3','line 4', 'line 5']
for line in lines:
    f.write(line + '\n')
f.close()