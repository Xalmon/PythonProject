class Account:
    accounts = []

    def __init__(self, first_name, last_name, pin):
        self.account_number = self.generate_account_number()
        self.first_name = first_name
        self.last_name = last_name
        self.pin = pin
        self.balance = 0
        self.accounts.append(self)

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount, pin):
        amount_is_positive = amount > 0
        sufficient_funds = self.balance >= amount
        correct_pin = pin == self.pin

        if amount_is_positive and sufficient_funds and correct_pin:
            self.balance -= amount

    def update_pin(self, new_pin):
        self.pin = new_pin

    def get_pin(self):
        return self.pin

    @classmethod
    def get_accounts(cls):
        return cls.accounts

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.pin}"

    def get_account_number(self):
        return self.account_number

    account_counter = 0

    def generate_account_number(self):
        Account.account_counter += 1
        return str(Account.account_counter)
