from banner import banner
banner("PYTHAGOREAN CALCULATOR", "Andrew Curnett")
again = 'Y'
error_1 = ("Sorry, you may only leave 1 side blank")
print("Welcome to the Pythagorean Calculator")
print("We will help you find the missing side length of a right triangle. The lengths of two legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")
print("")
input("Press the 'enter' key to begin.")
print("")
while again.upper() == 'Y':
    print("Please enter the length of each side, or leave it blank if you don't know.")
    print("")
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")

    if a == "" and b == "":
        print("")
        print(error_1)
        print("")
        input("Press the 'enter' key to try again")
        print("")
        continue

    elif a == "" and c == "":
        print("")
        print(error_1)
        print("")
        input("Press the 'enter' key to try again")
        print("")
        continue

    elif c == "" and b == "":
        print("")
        print(error_1)
        print("")
        input("Press the 'enter' key to try again")
        print("")
        continue

    elif a == "" and b == "" and c == "":
        print("")
        print(error_1)
        print("")
        input("Press the 'enter' key to try again")
        print("")
        continue
    elif a == "":
        b = float(b)
        c = float(c)
        a = ((c*c) - (b*b))**.5
        print("")
        print(f"your missing side length is {a}")
        print("")

    elif b == "":
        a = float(a)
        c = float(c)
        b = ((c*c) - (a*a))**.5
        print("")
        print(f"your missing side length is {b}")
        print("")

    elif c == "":
        b = float(b)
        a = float(a)
        c = ((a*a) + (b*b))**.5
        print("")
        print(f"your missing side length is {c}")
        print("")


    again = input("Would you like to calculate another triangle?(Y/N) ")

    if again.upper() == 'Y':
        print('\n' * 3)
        continue

    if again.upper() == 'N':
        print('\n' * 100)
        break


