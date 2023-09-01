class Account:
    def __init__(self, first_name, last_name, account_number, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.balance = 0
        self.pin = 1

    def withdraw(self, param, param1):
        pass

    def deposit(self, param):
        pass

    def update_pin(self, param):
        pass

    def get_pin(self):
        pass

    def transfer(self, param, param1, param2):
        pass

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.account_number}"

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance








