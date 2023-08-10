import re


def validate_email():
    return input("Enter a valid Email: ")


def is_email_valid(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)


def check_if_special_character_start_email(email):
    return re.match(r'^[^@]', email)


def check_if_special_character_end_email(email):
    return re.search(r"[^@]$", email)


def check_valid_email(email):
    if not check_if_special_character_start_email(email):
        print("Incorrect email: Should start with a valid character.")
        return False
    if not check_if_special_character_end_email(email):
        print("Incorrect email: Should end with a valid character.")
        return False
    if not is_email_valid(email):
        print("Incorrect email: Not a valid email format.")
        return False
    return True


def user_entry():
    email = validate_email()
    if check_valid_email(email):
        print("Wow, you've got a valid email! Congrats!")
    else:
        user_entry()


if __name__ == "__main__":
    user_entry()
