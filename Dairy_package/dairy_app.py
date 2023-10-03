from Dairy_package.Dairy import Diary


def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    diary = Diary(username, password)

    while True:
        print("\nOptions:")
        print("1. Unlock Diary")
        print("2. Lock Diary")
        print("3. Create Entry")
        print("4. List Entries")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            password_attempt = input("Enter your password to unlock: ")
            diary.unlock_diary(password_attempt)
        elif choice == "2":
            diary.lock_diary()
        elif choice == "3":
            if not diary.is_locked:
                title = input("Enter entry title: ")
                body = input("Enter entry body: ")
                diary.create_entry(title, body)
            else:
                print("Diary is locked. Unlock it first.")
        elif choice == "4":
            diary.list_entries()
        elif choice == "5":
            print("Bye Bye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
