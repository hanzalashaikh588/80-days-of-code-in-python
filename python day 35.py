# else statements in for loop\while loop
for i in range(10):
    print(i+1)
else:
    print('sorry there is no i')
# #else block prints only when statement is complete not when break is used!
for i in []:
    print(i)
else:
    print('sorry there is no i')
# break in else for loops
for i in range(15):
    print(i+1)
    if (i ==9):
        break
    else:    # here the if else makes a block and causes it to print else after every number until 9
              #to counter this we remove indentation from else and put else in the for loop indent.
     print("sorry there is no i")

# quiz
for i in range(10):
    print(i+1)
    if (i == 12):
        break
else:
    print("the loop was completed")
# while loops
i = 0
while i < 10:
    i =(i+1)
    print(i)
    if (i==12):
        break
else:
    print("statement is finished")