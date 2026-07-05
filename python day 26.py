#A SIMPLE PROGRAM THAT GREETS USER BASED ON THEIR TIME
hour = int(input('enter time : '))
print(hour)
if hour >= 0 and hour < 12:
    print("Good morning Sir")
elif hour >=12 and hour <17:
    print("Good afternoon Sir")
elif(hour>=17 and hour <0):
    print("good night sir")