import random

from banner import banner

banner("ROCK PAPER SCISSORS", "Amber Thompson and Andrew Curnett")

# Process
#1. Display game rules and say you will be playing best 2 out of 3.
#2. Ask player "rock, paper, or scissors"
#3. Compare players choice with the computers.
#4. First to 2 wins, game ends.
#5. Good game!

print("We are going to play the game Rock, Paper, Scissors. The first to win 2 games, wins.")

the_number = random.randint(1, 3)

print("Choose between these 3 options.")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
guess = int(input("Type the number of the option you choose. "))

if guess == 1:
    if the_number == 1:
        print(f"You have chose rock. The computer has chosen rock.")

if guess == 1:
    if the_number == 1:
        print("You have tied, let's go again.")

if guess == 2:
    if the_number == 2:
        print("You have chosen Paper, the computer has chosen paper.")
        print("You have tied, let's go again.")

if guess == 2:
    if the_number == 3:
        print("You have chosen paper, the computer has chosen Scissors")
        print("The computer has won this round.")







