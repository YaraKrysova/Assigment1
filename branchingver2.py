#I found anoyher way and it seems more efficent 
# for unknown reasons vs code refuses to create new branch to show all stages, 
# so i'll do it in different files

import random

myList = ("R", "P", "S")

computerChoice = random.choice(myList)

userChoice = input("Choose Rock (R), Paper (P), or Scissors (S): ")

if (userChoice == "S" and computerChoice == "P") or (userChoice == "P" and computerChoice == "R") or (userChoice == "R" and computerChoice == "S"):
    print("Computer: " + computerChoice)       
    print("You won")

elif userChoice == computerChoice:
    print("Computer: " + computerChoice)
    print("Try again")

elif userChoice is not ("R" or "P" or "S"):     #that part work strange, I should deal with it
    print("DO YOU ASSUME I AM A SORT OF AI TO UNDERSTAND SOMETHING ELSE?! I'm disappointed")
    print("Try again.")


else:
    print("Computer: "  + computerChoice)
    print("You loose")