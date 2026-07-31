marks=[34,46,87,93,68,24,0]
#without enumerate 
# index=0
# for mark in marks:
#     print(mark)
#     if (index==3):
#         print("highest marks")
#     if (index==6):
#         print("lowest marks")
#     index +=1
#enumerate function
for index , mark in enumerate(marks):
    print(mark)
    if (index==3):
        print("highest marks")
    if (index==6):
        print("lowest marks")

fruits=["mango","pineapple","apple","strawberry"]
for index, fruit in enumerate(fruits):
    if (index==0):
        print("the king of fruits")
    print(index,fruit)

teams=["real madrid","barcelona","man city","man united","ac milan"]
for index, team in enumerate(teams):
    print(f"{index +1} : {team}")
