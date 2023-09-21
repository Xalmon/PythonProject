from datetime import datetime


class Entry:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.date_created = datetime.now()


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_locked = True
        self.entries = []

    def unlock_diary(self, password):
        if self.password == password:
            self.is_locked = False
            print("Diary unlocked.")

    def lock_diary(self):
        self.is_locked = True
        print("Diary locked.")

    def is_locked(self):
        return self.is_locked

    def create_entry(self, title, body):
        if not self.is_locked:
            new_entry = Entry(len(self.entries), title, body)
            self.entries.append(new_entry)
            print("Entry created.")

    def list_entries(self):
        if not self.is_locked:
            print("Entries:")
            for entry in self.entries:
                print(f"ID: {entry.id}, Title: {entry.title}, Date: {entry.date_created}")


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
