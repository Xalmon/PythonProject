from datetime import datetime
from Dairy_package.Entry import Entry


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
                print(f"ID: {entry.id}, Title: {entry.title}")
                print(f"Date: {entry.date_created}")
                print(f"Body: {entry.body}\n")

