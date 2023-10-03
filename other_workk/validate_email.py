import re


def validate_email(email):
    if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return True
    else:
        return False


def check_emails(email_list):
    valid_emails = []

    for email in email_list:
        if email.startswith('@') or email.endswith('@') or email.count('@') != 1:
            print(f"Invalid email: {email} - Starts or ends with '@', or has multiple '@' symbols")
        elif email.endswith('.com') and len(email) >= 6 and validate_email(email):
            valid_emails.append(email)
        else:
            print(f"Invalid email: {email} - Doesn't meet criteria")

    return valid_emails


def user_entry():
    num_emails = input("Enter the number of emails: ")
    email_list = []

    for _ in range(num_emails):
        email = input("Enter an email: ")
        email_list.append(email)

    valid_emails = check_emails(email_list)

    print("\nValid emails:")
    for email in valid_emails:
        print(email)


if __name__ == "__main__":
    user_entry()
