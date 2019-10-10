from banner import banner
import random

banner("Lottery", "Andrew Curnett")
again = 'Y'
print("Welcome to the Lottery game. Choose a number between 1 and 100, if you choose the same number as the computer, you will win 10 times your bet ammount.")

balance = 20
print("")
print(f"BALANCE: ${balance}")

while again:

    cpu_guess = random.randint(1, 1)
    bet = int(input("How much do you want to bet? $"))
    if bet > balance:
        print("Sorry, not enough funds in balance, please try again.")
        continue
    balance = balance - bet
    p_guess = int(input("What number do you pick? "))
    if p_guess < 1 or p_guess > 100:
        print("Sorry, please choose a number between 1 and 100")
        balance = balance + bet
        continue
    elif p_guess == cpu_guess:
        balance = balance + bet * 10
        print(f"Congratulations! You chose {p_guess} and the computer also chose {cpu_guess}!, you win {bet * 10}!")
        print(f"BALANCE: ${balance}")
    else:
        print(f"Sorry, you chose {p_guess} and the computer chose {cpu_guess}, you lose ${bet} this round.")
        print("")
        print(f"BALANCE: ${balance}")
        print("")
    if balance > 999999:
        print("You have reached reached maximum funds! You win! Thanks for playing!")
        input("Click the 'enter' key to end.")
        print('\n' * 100)
        break
    if balance == 0:
        print("Sorry, no more funds.")
        input("Click the 'enter' key to end.")
        print('\n' * 100)
        break
    again = input("Would you like to play again?(Y/N) ")
    if again.upper() == 'Y':
        print('\n' * 2)
        continue
    if again.upper() == 'N':
        print("Thanks for playing!")
        input("Click the 'enter' key to end.")
        break



