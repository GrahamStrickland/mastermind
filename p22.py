# Array of letters representing colours, and keys representing scores.
# secretCode will be used to store a randomly generated code, userGuess
# will be used to store guesses that will be scored using score array.
from math import floor
from random import random

colours = ['R', 'W', 'Y', 'G', 'Bu', 'Bk']
keys = ['b', 'w']
positions = 4
secretCode = []
userGuess = []
score = []
guess = ""

# Function to generate random integers within range.
def getRandomInt(max):
    return floor(random() * max)

# Generate random secret code.
for i in range(positions):
    secretCode.append(colours[getRandomInt(len(colours))])

# Enter user guess and output score.
print("You must guess a secret code made up of " + str(positions), end="")
print(" of the following colours:")
print("Red (R), white (W), yellow (Y), green (G), blue (Bu), or black (Bk).")
for i in range(positions):
    # Input user guess
    print("Please enter a colour:")
    guess = str(input("> "))
    while (guess not in colours):
        print("Please enter a valid input from the following")
        for colour in colours:
            print(colour, "\t", end="")
        print('')
        guess = str(input("> "))
    userGuess.append(guess)
    
    # Add score to array
    if (userGuess[i] == secretCode[i]):
        score.append(keys[0])
    elif (userGuess[i] in secretCode):
        score.append(keys[1])

# Output score array
print("\nScore for User\'s Guess:")
for key in score:
    print(key, '\t', end="")
print('')
