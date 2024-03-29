import datetime
from banner import banner

banner("BIRTHDAY", "Andrew Curnett")

# Process
# 1. Find out birthday from user
# 2. Calculate how many days apart that is from now
# 3. Print the birthday info, Days to go, Days ago, or Happy BDay!

def main():
    birthday = get_birthday_from_user()
    now = datetime.date.today()
    num_days = calculate_days_between_dates(birthday, now)
    print_birthday_info(num_days)

def get_birthday_from_user():
    print("What is your birthday?")
    year = int(input("Year [YYYY]? "))
    month = int(input("Month [MM] "))
    day = int(input("Day [DD] "))

    birthday = datetime.date(year, month, day)
    return birthday

def calculate_days_between_dates(date1, date2):
    this_year = datetime.date(date2.year, date1.month, date1.day)
    dt = this_year - date2
    return dt.days

def print_birthday_info(number_of_days):
    if number_of_days > 0:
        print(f"Your birthday is in {number_of_days} days. Can't wait!")
    elif number_of_days < 0:
        print(f"Your birthday was {-number_of_days} days ago. Can't wait for the next one!")
    else:
        print("Today's your birthday! Happy Birthday!")





main()








