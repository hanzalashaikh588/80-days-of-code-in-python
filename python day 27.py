def main_program():
    name = input("enter your name : ")
    print("Welcome to the game!" , name)
    print("here are 3 questions that u will be answering today", name , "for a chance to win 1 million dollars. ")
    question1 = print('1. who won the fifa worldcup in 2014? ')
    Ans =(input("enter your answer : "))
    ans1 = ('germany')
    if(ans1 == Ans):
        print("That is correct!")
    else:
        print("You are wrong game over")
        return
    question2= print("2. who is the only woman in history to win 2 nobel prizes?")
    Ans2c=(input("enter your answer : "))
    ans2= ("marie curie")
    if(ans2==Ans2c):
        print(" you are correct!")
    else:
        print(" you are wrong")
        return
    print("now do you wish to continue? remeber if you get this answer wrong you lose all of your money or you may leave now.")
    do = input("enter yes or no :" )
    if do == 'yes':
        print("Now for the last question")
    else:
        print("thank you for playing")
        return
    question3 = print("3. what is the captal of Thailand")
    Ans3c=(input("enter your answer : "))
    ans3=("bangkok")
    if(ans3==Ans3c):
        print("congratulations you have won the 1 million dollar prize!")
    else:
        print("unfortunately you are wrong and have lost all your prize money.")
    print("thank you for playing")
if __name__=="__main__":
     while True:
         main_program()

         again=input("do you wish to try again?(y/n) : ")
         if again not in ["y", "yes"]:
            print("Goodbye")
            break

            








