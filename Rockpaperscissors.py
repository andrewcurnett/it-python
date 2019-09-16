import random

from banner import banner

banner("ROCK PAPER SCISSORS", "Amber Thompson and Andrew Curnett")

# Process
#1. Display game rules and say you will be playing best 2 out of 3.
#2. Ask player "rock, paper, or scissors"
#3. Compare players choice with the computers.
#4. First to 2 wins, game ends.
#5. Good game!
player_name = input("Hi, I am 'the computer', What is your name? ")
print("")
print(f"Nice to meet you, {player_name}, We are going to play the game Rock, Paper, Scissors. The first to win 2 games, wins.")
print("")
input("Press the 'enter' key to begin.")

computer_score = 0
player_score = 0


while player_score < 2 and computer_score < 2:
    print("")
    print("=========SCORE=========")
    print(f"Computer - {computer_score}")
    print(f"{player_name} - {player_score}")
    print("_______________________")
    print("")

    the_number = random.randint(1, 3)

    print("")
    print("Choose between these 3 options.")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("")
    guess = int(input("Type the number of the option you choose. "))
    print("")


    if guess == 1:
        if the_number == 1:
            print("You have chose rock. The computer has chosen rock.")
            print("You have tied, we go again!")
            print("")
            input("Press the 'enter' key to move forward.")
            print("")
        elif the_number == 2:
            print("You have chosen rock, the computer has chosen paper.")
            print("The computer has won this round, EZZZ CLEPS, better luck next round nerd, GR")
            computer_score = computer_score + 1
            print("")
            input("Press the 'enter' key to move forward.")
            print("")
        elif the_number == 3:
            print("You have chosen rock, the computer has chosen scissors.")
            print("You have won this round, computer got clepped, GR kid.")
            player_score = player_score + 1
            print("")
            input("Press the 'enter' key to move forward.")
            print("")

    if guess == 2:
        if the_number == 1:
            print("You have chosen paper, the computer has chosen Rock.")
            print("You, my friend, have won this round. GR")
            player_score = player_score + 1
            print("")
            input("Press the 'enter' key to move forward.")
            print("")
        elif the_number == 2:
            print("You have chosen Paper, the computer has chosen paper.")
            print("You have tied, let's go again.")
            print("")
            input("Press the 'enter' key to move forward.")
            print("")
        elif the_number == 3:
            print("You have chosen paper, the computer has chosen Scissors")
            print("The computer has won this round.")
            computer_score = computer_score + 1
            print("")
            input("Press the 'enter' key to move forward.")
            print("")

    if guess == 3:
        if the_number == 1:
            print("You have chosen scissors, the computer has chosen rock")
            print("The computer has won this round, ez cleps gr m8")
            computer_score = computer_score + 1
            print("")
            input("Press the 'enter' key to move forward.")
            print("")
        elif the_number == 2:
            print("You have chosen scissors, the computer has chosen paper")
            print("You have won this round, but you still suck, GR m8")
            player_score = player_score + 1
            print("")
            input("Press the 'enter' key to move forward.")
            print("")
        elif the_number == 3:
            print("You have chosen scissors, the computer has chosen scissors")
            print("You have tied, and so it continues. gr")
            print("")
            input("Press the 'enter' key to move forward.")
            print("")
print("")
if computer_score > 1:
    print("=========SCORE=========")
    print(f"Computer - {computer_score}")
    print(f"{player_name} - {player_score}")
    print("_______________________")
    print("")
    print("The computer has won this game, better luck next time, NERD")

if player_score > 1:
    print("=========SCORE=========")
    print(f"Computer - {computer_score}")
    print(f"{player_name} - {player_score}")
    print("_______________________")
    print("")
    print("The computer has been beaten, gg good fella")




