
userChoice = input("Choose Rock (R), Paper (P), or Scissors (S): ")


import random
mylist = ["R", "P", "S"]



if (userChoice == "S" and random.choice(mylist) == "P") or (userChoice == "P" and random.choice(mylist) == "R") or (userChoice == "R" and random.choice(mylist) == "S"):
    print("Computer: ")
    print("You won")

#elif userChoice == "P" and random.choice(mylist) == "R":
    #print("Computer: R")
    #print("You won")

#elif userChoice == "R" and random.choice(mylist) == "S":
    #print("Computer: S")
    #print("You won")

elif userChoice == random.choice(mylist):
    print("Computer: same")
    print("Try again")

else:
    print("Computer: "  + random.choice(mylist))
    print("You loose")