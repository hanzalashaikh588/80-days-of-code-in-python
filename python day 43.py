#import in python
# import math
# squareroot = math.sqrt(144)
# print(squareroot)

# #from 
# from math import sqrt , pi
# result = sqrt(9) * pi
# print(result)
# print(pi)
#  #as keyword
# from math import pi as pie , sqrt as s
# result = s(9) * pi
# print(result)
# print(pie)

#random
def number_guessing_game():
    print("welcome to the number guessing game!")
    import random
    secret_number = random.randint(1,10)
    print("guess a number between 1 and 10")
    guess = int(input("enter your guess (1-10) : "))
    if secret_number == guess:
        print("goodjob")
    else:
        print("wrong")
    ask= input("do you wish to try again?:  ")
    if ask == "yes":
        return
    if ask == "no":
        print("Goodbye")
        return
number_guessing_game()

# def number_generator():
#     print("welcome to the number generator")
#     import random
#     y = random_numbers=random.randint(1,100)
#     ask = input("do you wish to generate your number? ")
#     if ask=="yes" : 
#          print(y)
#     if (ask== "no"):
#             print("goodbye")
# number_generator()