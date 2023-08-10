import re
import time


def user_entry():
    user = input("Enter password: ")
    conditions(user)


def conditions(user=None):
    if len(user) < 8:
        print("The password you selected is too short")
        user_entry()
        return False

    if not re.search("[A-Z]", user):
        print("Please start with uppercase(capital) letters in your password")
        user_entry()
        return False

    if not re.search("[a-z]", user):
        print("You are required to add lowercase(small) letters to your password")
        user_entry()
        return False

    if not re.search('[0-9]', user):
        print("Also another requirement is to add digits(numbers) to your password")
        user_entry()
        return False

    if not re.search('[#?!@$%^&*-]', user):
        print("To ensure safety another requirement is to add special character (#?!@$%^&*-)")
        user_entry()
        return False

    else:
        password_validation(user)
        print("wow,you've got a valid password! Congrats!")
        save()


def save():
    print("Saving", end="")
    for n in range(0, 3):
        print(">", end="")
        time.sleep(1)

    print("\nNow your password has been saved successfully")


def password_validation(user=None):
    user_check = input("\nYou're doing great,re-enter the password: ")

    while user != user_check:
        print("\nError! password mis-match, re-enter correct password")
        user_entry()
        password_validation()


if __name__ == "__main__":
    user_entry()
