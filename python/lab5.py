#Number Guessing Game

import random
randnum = random.randint(1,100)
#Generating Random Number via the Imported Module

usrguess = int(input("Guess a postive real number between 1 and 100\n"))
#Promting the User to Input their Guess

while True:
        if usrguess == randnum:
            print("Correct")
            break
        elif usrguess > randnum:
            print("Too High")
            usrguess = int(input("Guess Again\n"))
        elif usrguess < randnum:
            print("Too Low")
            usrguess = int(input("Guess Again\n"))

  