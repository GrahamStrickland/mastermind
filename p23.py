# MASTERMIND CLI GAME
# Array of letters representing colours, and keys representing scores.
# secretCode will be used to store a randomly generated code, userGuess
# will be used to store guesses that will be scored using score array.
from math import floor
from random import random


# VARIABLE INITIALIZATION
colours = ['R', 'W', 'Y', 'G', 'Bu', 'Bk']
keys = ['\u25CF', '\u25CB']
positions = 4
secretCode = []
userGuess = []
score = []
guess = ""
rounds = 0
turns = 0
wins = 0
ans = ''
gameOver = False
forfeit = False


# Function to generate random integers within range.
def getRandomInt(max):
    return floor(random() * max)


# ROUND INITIALIZATION SECTION
while (ans != 'N' and ans != 'n'):
    # Reset turns for next round and print information.
    gameOver = False
    forfeit = False
    turns = 0
    if (rounds == 0):
        print('*' * 70)
        print("\t\t\tMASTERMIND")
        print('*' * 70)
        print("Guess a secret code made up of " + str(positions), end="")
        print(" of the following coloured pegs:")
        print("Red (R), white (W), yellow (Y), green (G), blue (Bu), or black (Bk).")
        print("For each guess a score is awarded as follows:")
        print(f"{keys[0]} = right colour, right position.")
        print(f"{keys[1]} = right colour, wrong position.")
        print("A maximum of one key is awarded per coloured peg in the user\'s guess.")
        print("F = forfeit round.")
    print('+' * 70)
    print(f"Round {rounds+1}!")
    print('+' * 70)
    
    # Generate random secret code.
    for i in range(positions):
        if rounds == 0:
            secretCode.append(colours[getRandomInt(len(colours))])
        else:
            secretCode[i] = colours[getRandomInt(len(colours))]
    print("Secret Code = ", end="")
    print(secretCode)


# GUESSING SECTION
    while not gameOver:
        # Reset score array and guess array.
        score = [None for i in range(positions)]
        userGuess = [None for i in range(positions)]

        # Input user guess.
        print("Please enter one colour for each position.")
        for i in range(positions):
            print(f"{i+1}", end="")
            guess = str(input(": ")).title()
            if guess == 'f' or guess == 'F':
                forfeit = True
                break
            else:
                while guess not in colours:
                    if guess == 'f' or guess == 'F':
                        forfeit = True
                        break
                    print("Please enter a valid input from the following")
                    for colour in colours:
                        print(colour, "\t", end="")
                    print('')
                    guess = str(input("> ")).title()
            if forfeit:
                break
            else:
                userGuess[i] = guess


# SCORING SECTION
        if not forfeit:
            for i in range(positions):
                # Assign keys for right colour, right position.
                if userGuess[i] == secretCode[i]:
                    score[i] = keys[0]

            for i in range(positions):
                # Assign keys for right colour, wrong position.
                if userGuess[i] == secretCode[i]:
                    pass
                elif userGuess[i] in secretCode:
                    for j in range(positions):
                        if i != j and userGuess[i] == secretCode[j]:


# END OF TURN/ROUND SECTION
        # Output win or result from score array.
        if all(key == keys[0] for key in score):
            gameOver = True
            wins = wins + 1
            rounds = rounds + 1
            if turns == 0:
                print(f"You guessed correctly after {turns+1} turn!")
            else:
                print(f"You guessed correctly after {turns+1} turn/s!")
            print(f"Computer: {rounds-wins}, User: {wins}")
            print("Would you like to play again? (Y/N)")
            ans = str(input("> "))
            while ans != 'N' and ans != 'n' and ans != 'Y' and ans != 'y':
                ans = str(input("Invalid input! Please enter Y or N."))
        elif forfeit:
            gameOver = True
            rounds = rounds + 1
            print("You forfeit this round, the computer wins!")
            print(f"Computer: {rounds-wins}, User: {wins}")
            print("Would you like to play again? (Y/N)")
            ans = str(input("> "))
            while ans != 'N' and ans != 'n' and ans != 'Y' and ans != 'y':
                ans = str(input("Invalid input! Please enter Y or N."))
        else:
            print('-' * 70)
            print("\t\tGuess\t\tScoring")
            print('-' * 70)
            print(f"Guess {turns+1}:\t", end="")
            for colour in userGuess:
                print(colour, ' ', end="")
            print('\t', end="")
            for key in score:
                if key == keys[0]:
                    print(key, ' ', end="")
            for key in score:
                if key == keys[1]:
                    print(key, ' ', end="")
            print('\n')
            turns = turns + 1

print("Thank you for playing Mastermind, goodbye!")
