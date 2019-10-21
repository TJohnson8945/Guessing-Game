"""
Guessing Game
Author: Tyler Johnson

Player needs to guess the # the computer is thinking
Computer needs to pick a number between range of 1 - 100
Needs to request the player to input a number
Computer needs to inform player wether the guess is too high or too low
Needs to keep track of how many guesses it has taken



"""
import random

number = random.randint(1, 100)
numberGuess = 0

print ("Let's play a game. I'm gonna come up with a random number between 1 and 100 and you guess!")
print()
guess = int(input("Okay, what is your guess? "))

while number != "guess":
    
    if guess > number:
        print()
        print (str(guess) + " Is too high!")
        guess = int(input("Try again! "))
        numberGuess += 1
        
    elif guess < number:
        print()
        print (str(guess) + " Is too low!")
        guess = int(input("Try again! "))
        numberGuess += 1

    else:
        numberGuess += 1
        print()
        print (str(guess) + " Was it! Look at you go! It took you " + str(numberGuess) + " tries!")
        break

