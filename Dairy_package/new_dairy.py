import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class Diary:
    def __init__(self, root):
        self.datetime = datetime
        self.root = root
        self.root.title("Diary App")

        self.create_diary_button = tk.Button(root, text="Create Diary", command=self.create_diary)
        self.create_diary_button.pack()

        self.set_password_button = tk.Button(root, text="Set Password", command=self.set_password, state=tk.DISABLED)
        self.set_password_button.pack()

        self.unlock_button = tk.Button(root, text="Unlock Diary", command=self.unlock_diary, state=tk.DISABLED)
        self.unlock_button.pack()

        self.lock_button = tk.Button(root, text="Lock Diary", command=self.lock_diary, state=tk.DISABLED)
        self.lock_button.pack()

        self.create_entry_button = tk.Button(root, text="Create Entry", command=self.create_entry, state=tk.DISABLED)
        self.create_entry_button.pack()

        self.list_entries_button = tk.Button(root, text="List Entries", command=self.list_entries, state=tk.DISABLED)
        self.list_entries_button.pack()

        self.text_widget = tk.Text(root, height=10, width=40)
        self.text_widget.pack()

        self.is_locked = True
        self.password = "password"
        self.entries = []

    def create_diary(self):
        self.datetime.now()
        self.set_password_button.config(state=tk.NORMAL)
        self.unlock_button.config(state=tk.DISABLED)
        self.lock_button.config(state=tk.DISABLED)
        self.create_entry_button.config(state=tk.DISABLED)
        self.list_entries_button.config(state=tk.DISABLED)
        self.text_widget.insert(tk.END, "Diary created. You can now set a password.\n")

    def set_password(self):
        if self.is_locked:
            password_window = tk.Toplevel(self.root)
            password_window.title("Set Password")

            password_label = tk.Label(password_window, text="Set a new password:")
            password_label.pack()
            password_entry = tk.Entry(password_window, show="*")
            password_entry.pack()

            submit_button = tk.Button(
                password_window,
                text="Set Password",
                command=lambda: self.save_password(password_entry.get(), password_window),
            )
            submit_button.pack()
        else:
            self.text_widget.insert(tk.END, "Diary must be locked to set a new password.\n")

    def save_password(self, new_password, window):
        if new_password:
            self.password = new_password
            window.destroy()
            self.text_widget.insert(tk.END, "Password set successfully!\n")
            self.unlock_button.config(state=tk.NORMAL)
            self.set_password_button.config(state=tk.DISABLED)
        else:
            self.text_widget.insert(tk.END, "Password cannot be empty.\n")

    def unlock_diary(self):
        entered_password = self.get_password()

        if entered_password == self.password:
            self.is_locked = False
            self.unlock_button.config(state=tk.DISABLED)
            self.set_password_button.config(state=tk.DISABLED)
            self.lock_button.config(state=tk.NORMAL)
            self.create_entry_button.config(state=tk.NORMAL)
            self.list_entries_button.config(state=tk.NORMAL)
            self.text_widget.insert(tk.END, "Diary unlocked.\n")
        else:
            self.text_widget.insert(tk.END, "Incorrect password.\n")

    def lock_diary(self):
        self.is_locked = True
        self.unlock_button.config(state=tk.NORMAL)
        self.lock_button.config(state=tk.DISABLED)
        self.create_entry_button.config(state=tk.DISABLED)
        self.list_entries_button.config(state=tk.DISABLED)
        self.text_widget.insert(tk.END, "Diary locked.\n")

    def create_entry(self):
        if not self.is_locked:
            entry_window = tk.Toplevel(self.root)
            entry_window.title("Create Entry")

            title_label = tk.Label(entry_window, text="Title:")
            title_label.pack()
            title_entry = tk.Entry(entry_window)
            title_entry.pack()

            body_label = tk.Label(entry_window, text="Body:")
            body_label.pack()
            body_entry = tk.Text(entry_window, height=5, width=30)
            body_entry.pack()

            save_button = tk.Button(
                entry_window,
                text="Save Entry",
                command=lambda: self.save_entry(title_entry.get(), body_entry.get("1.0", tk.END)),
            )
            save_button.pack()

            entry_window.mainloop()
        else:
            self.text_widget.insert(tk.END, "Diary is locked. Unlock it first.\n")

    def save_entry(self, title, body):
        if not self.is_locked:
            entry = {
                "title": title,
                "body": body,
                "date_created": self.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.entries.append(entry)
            self.text_widget.insert(tk.END, "Entry saved.\n")
        else:
            self.text_widget.insert(tk.END, "Diary is locked. Unlock it first.\n")

    def list_entries(self):
        if not self.is_locked:
            self.text_widget.insert(tk.END, "Entries:\n")
            for idx, entry in enumerate(self.entries, start=1):
                self.text_widget.insert(
                    tk.END, f"Entry {idx} - Title: {entry['title']}, Date: {entry['date_created']}\n"
                )
        else:
            self.text_widget.insert(tk.END, "Diary is locked. Unlock it first.\n")

    def get_password(self):
        password_window = tk.Toplevel(self.root)
        password_window.title("Enter Password")

        password_label = tk.Label(password_window, text="Enter password:")
        password_label.pack()
        password_entry = tk.Entry(password_window, show="*")
        password_entry.pack()

        submit_button = tk.Button(
            password_window,
            text="Submit",
            command=lambda: self.check_password(password_entry.get(), password_window),
        )
        submit_button.pack()

    def check_password(self, entered_password, window):
        if entered_password == self.password:
            window.destroy()
            self.is_locked = False
            self.unlock_button.config(state=tk.DISABLED)
            self.set_password_button.config(state=tk.DISABLED)
            self.lock_button.config(state=tk.NORMAL)
            self.create_entry_button.config(state=tk.NORMAL)
            self.list_entries_button.config(state=tk.NORMAL)
            self.text_widget.insert(tk.END, "Diary unlocked.\n")
        else:
            self.text_widget.insert(tk.END, "Incorrect password.\n")


def main():
    root = tk.Tk()
    app = Diary(root)
    root.mainloop()


if __name__ == "__main__":
    main()
