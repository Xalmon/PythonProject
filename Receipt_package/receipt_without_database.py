user_info_list = []


def receipt_info():
    name = input("Enter name: ")
    address = input("Enter address: ")
    telephone = input("Enter telephone: ")
    email = input("Enter email: ")

    user_info_list.append({
        'name': name,
        'address': address,
        'telephone': telephone,
        'email': email
    })

    print("User information saved successfully!")


def print_receipt_info():
    if not user_info_list:
        print("No user information available.")
    else:
        for idx, user in enumerate(user_info_list, start=1):
            print(f"User {idx}:")
            print(f"Name: {user['name']}")
            print(f"Address: {user['address']}")
            print(f"Telephone: {user['telephone']}")
            print(f"Email: {user['email']}\n")


while True:
    print("Options:")
    print("1. Enter receipt information")
    print("2. Print receipt information")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        receipt_info()
    elif choice == "2":
        print_receipt_info()
    elif choice == "3":
        break
    else:
        print("Invalid option. Please choose a valid option.")
