#   Assigment 1
#   Class:1249_83333
#   Krysova Iaroslava

import random

print("                  --Arrogant rock paper scissors game-- ")  #I gave him more personality
print("I bet you'll never win me")
print("However, you can try, here's the rules:")
print("Scissors beats paper, paper beats rock and rock beats scissors. If you'll realise that you'll never win me, write ESCAPE")
print(" ")

gameAmount = int(input("How many rounds you are expecting to loose? "))     #Amount of games in which ether user or computer would win

print("alright... let's start")
print(" ")


def oneGame():

    userWinAmount = 0       # how much user would win
    computerWinAmount = 0       # how much computer would win

    while (gameAmount > userWinAmount) or (gameAmount > computerWinAmount):       #It's not stopping... why? upd: I put break and continue functions, now it's fine

        myList = ("R", "P", "S")    #I decided to put this piece of code in the main file because it's easier for me to control

        computerChoice = random.choice(myList)

        userChoice = input("Choose Rock (R), Paper (P), or Scissors (S): ")

        if (userChoice == "S" and computerChoice == "P") or (userChoice == "P" and computerChoice == "R") or (userChoice == "R" and computerChoice == "S"):
            print("Computer: " + computerChoice)       
            print("You won, what a coincedence...")
            userWinAmount = userWinAmount + 1
            print(f"Score: {userWinAmount} : {computerWinAmount}")

        elif userChoice == computerChoice:
            print("Computer: " + computerChoice)
            print("It's a tie")

        elif userChoice == "ESCAPE":    #in case user would like to finish earlier
            print("You gave up too early? Alright, goodbye")
            break

        #elif userChoice is not ("R" or "P" or "S"):     #that part work strange, I should deal with it
            print("DO YOU ASSUME I AM A SORT OF AI TO UNDERSTAND SOMETHING ELSE?! I'm disappointed")
            print("Try again.")

        elif(computerChoice == "S" and userChoice == "P") or (computerChoice == "P" and userChoice == "R") or (computerChoice == "R" and userChoice == "S"):
            print("Computer: "  + computerChoice)
            print("You loose")
            computerWinAmount = computerWinAmount + 1
            print(f"Score: {userWinAmount} : {computerWinAmount}")

        else:
            print("DO YOU ASSUME I AM A SORT OF AI TO UNDERSTAND SOMETHING ELSE?! I'm disappointed")
            print("Try again.")




        if computerWinAmount == gameAmount:
            print("I won, which was predictable.")
            break
        elif userWinAmount == gameAmount:
            print("Unbelivable... you are actually good...")
            break


oneGame()

newGame = input("Do you want to play again? (Y/N) ")
if newGame == "Y":
    oneGame()

else:
    print("Alright... It was fun... See you again...")