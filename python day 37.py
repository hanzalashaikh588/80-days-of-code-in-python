#Finally keyword in python.
#finally is a keyword in python thats is always printed.
# def func1():
#     try:
#         l=[1 , 2 , 3 , 4 , 5]
#         i= int(input("select your index : "))
#         print(l[i])
#         return 1
#     except:
#             print("sorry some error has occured")
#             return 0
#     finally:
#         print("please pick a number from (0-4)")

# x=func1()
# print(x)
def func2():
    try:
        for i in range(1,11):
            print(i)
            if (i==12):
                print("12 has been printed")
            else:
                return
    finally:
        print("nothing stops this statement from being printed")
func2()

