# Guessing-Game
This project was assigned to my Python Programming class early on in the semester. It was our introduction to if statements.
Originally the project was just to have a set value as the games guess, but I decided to spice it up by adding the randint function.

## Getting Started
This program was created and runs on Python IDLE IDE in a command box.

## Explaining the Program

### Initialization
The first line is importing pythons random function.
Followed by initializing the number variable as a random number ranging from 1 to 100.
Then the variable numberGuess is initialized and set to zero.
This will be the counter for how many attempts it took to get the right number.

### Running the Program
The program starts by printing our the intstructions for the game.

It then requests an input from the user for the user's guess.

### Are they right or wrong?
The program then goes into a while loop that has an if statement nested right in. 

The while loop checks to see if the random number selected is not equal to the user's guess,
if it is not equal, then it proceeds into the if statement.

If the guess is greater than the number, it prints out that the guess is too high and prompts the user to
guess again, while incrementing the numberGuess variable one.

If the guess is less than the number, it prints out that the guess is too low and prompts the user to guess again,
while also incrementing the numberGuess variable one.

If the guess is correct, the program will increment numberGuess one last time, then output to the user that they were correct,
and how many attempts it took them to get to the correct answer!

This is followed by a break that was implemented simply to end the loop.

## Purpose
The intent of the project was to test my knowledge of while loops and if statements during my Python programming class. 
I felt confident, after doing this assignment, that I have a firm understanding of loops. This confidence has supported me in my further
pursuits as I have taken more difficult classes. I have my professor, Dr. Trifas, to thank for teaching me Python.
