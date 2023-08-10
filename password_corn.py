import re
import time


def get_password():
    return input("Enter password: ")


def is_valid_length(password):
    return len(password) >= 8


def has_uppercase(password):
    return re.search("[A-Z]", password)


def has_lowercase(password):
    return re.search("[a-z]", password)


def has_digit(password):
    return re.search("[0-9]", password)


def has_special_char(password):
    return re.search('[#?!@$%^&*-]', password)


def validate_password(password):
    if not is_valid_length(password):
        print("Password is too moyin.")
        return False

    if not has_uppercase(password):
        print("Password must contain uppercase letters.")
        return False

    if not has_lowercase(password):
        print("Password must contain lowercase letters.")
        return False

    if not has_digit(password):
        print("Password must contain digits.")
        return False

    if not has_special_char(password):
        print("Password must contain special characters (#?!@$%^&*-,>|;:+-_~.`)")
        return False

    return True


def save_password():
    while True:
        print("Saving", end="")
        for n in range(0, 3):
            print(">", end="")
            time.sleep(1)
        try:
            print("Saving", end="")
            for n in range(0, 3):
                print(">", end="")
                time.sleep(1)
            print("\nPassword saved successfully.")
            break
        except Exception as e:
            print("\nError saving password:", e)
            retry = input("Do you want to retry saving the password? (y/n): ")
            if retry.lower() != 'y':
                break


def user_entry():
    password = get_password()
    if validate_password(password):
        print("Wow, you've got a valid password! Congrats!")
        save_password()
    else:
        user_entry()


if __name__ == "__main__":
    user_entry()
