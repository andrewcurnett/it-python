from banner import banner
banner("ZIP CODE SORTER", "Andrew Curnett")

print("Welcome to the newaygo county zip code sorter.")

search_again = 'Y'
while search_again.upper() == 'Y':
    zip_code = input("Please enter your zip code: ")
    if zip_code == '49412':
        print(f"The zip code for {zip_code} is for Fremont")
        search_again = input("Would you like to enter another zip code?(Y/N) ")
    elif zip_code == '49309':
        print(f"The zip code for {zip_code} is for Bitely")
        search_again = input("Would you like to enter another zip code?(Y/N) ")
    elif zip_code == '49312':
        print(f"The zip code for {zip_code} is for Brohman")
        search_again = input("Would you like to enter another zip code?(Y/N) ")
    elif zip_code == '49337':
        print(f"The zip code for {zip_code} is for Croton and Newaygo")
        search_again = input("Would you like to enter another zip code?(Y/N) ")
    elif zip_code == '49413':
        print(f"The zip code for {zip_code} is for Fremont")
        search_again = input("Would you like to enter another zip code?(Y/N) ")
    elif zip_code == '49327':
        print(f"The zip code for {zip_code} is for Grant")
        search_again = input("Would you like to enter another zip code?(Y/N) ")
    elif zip_code == '49349':
        print(f"The zip code for {zip_code} is for White cloud")
        search_again = input("Would you like to enter another zip code?(Y/N) ")
    else:
        print("Not in Newaygo County")
        print('')
        continue

    if search_again.upper() == 'Y':
        print('\n' * 2)
        continue

    if search_again.upper() == 'N':
        print("Thank you for using Newaygo County Zip Code sorter. Goodbye!")
        input("Press the 'enter' key to end.")
        print('\n' * 100)