from datetime import datetime


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_locked = True
        self.entries = []
        self.id_generator = 1

    def create_entry(self, title, body):
        if not self.is_locked:
            new_entry = Entry(len(self.entries), title, body)
            self.entries.append(new_entry)

    def generate_id(self):
        id = self.id_generator
        self.id_generator += 1
        return id

    def unlock_diary(self, password):
        if self.password == password:
            self.is_locked = False

    def lock_diary(self):
        self.is_locked = True

    def is_locked(self):
        return self.is_locked


class Entry:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.date_created = datetime.now()
