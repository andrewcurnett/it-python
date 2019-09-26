from banner import banner
import random

banner("Lottery", "Andrew Curnett")

print("Welcome to the Lottery game. Choose a number between 1 and 100, if you choose the same number as the computer, you will win 10 times your bet ammount.")

cpu_guess = random.randint(1, 100)

balance = 20

print(f"BALANCE: ${balance}")