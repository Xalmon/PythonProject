import sqlite3

connection = sqlite3.connect("user_info.db")

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        address TEXT,
        telephone TEXT,
        email TEXT
    )
''')


def receipt_info():
    name = input("Enter name: ")
    address = input("Enter address: ")
    telephone = input("Enter telephone: ")
    email = input("Enter email: ")

    cursor.execute("INSERT INTO users (name, address, telephone, email) VALUES (?, ?, ?, ?)",
                   (name, address, telephone, email))
    connection.commit()
    print("User information saved successfully!")


def print_receipt_info():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    if not users:
        print("No user information available.")
    else:
        for user in users:
            print(f"User {user[0]}:")
            print(f"Name: {user[1]}")
            print(f"Address: {user[2]}")
            print(f"Telephone: {user[3]}")
            print(f"Email: {user[4]}\n")


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

connection.close()
