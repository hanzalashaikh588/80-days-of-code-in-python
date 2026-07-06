# f strings are used to include variables into strings and include integers into strings.
#old formatting before f strings were introduced in 3.6
letter="Hey my name is {1} and I am from {0}"
country="brazil"
name="charles"
print (letter.format(country,name))
#new formatting after f strings 
name="hanzala"
country="pakistan"
print(f"Hey my name is {name} and I am from {country}")
#example including integers.
price=99.99999
txt=f"for only {price:.0f} dollars!"#.2f here means only pick 2 decimals
print(txt)
#print(txt.format(price=99.99999))
#example using only integers,
int1=(f"{10*20}")
print(int1)
print(type(int1))# as you can see its type its a string
# if you need to print literally with f string.
name="hanzala"
country="pakistan"
print(f"Hey my name is {{name}} and I am from {{country}}")
#example of program using f
name=input("enter your name: ")
country=input("enter your country: ")
print(f"Your name is {name} and you live in {country}")
population=input(f"enter the population of your {country} : ")
population1="2000000"
if (population.replace(",","")==population1):
    print("thats correct!")
else:
    print(f" Thats wrong the population of {country} is {int(population1):,}.")

