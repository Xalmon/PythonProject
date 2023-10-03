from AccountPackage.Accounts import Account


class Bank:
    def __init__(self):
        self.accounts = []
        self.balance = 0

    def get_balance(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account.get_balance()
        return None

    def register(self, first_name, last_name, pin):
        account = Account(first_name, last_name, pin)
        self.accounts.append(account)

    def generate_account_number(self):
        return str(len(self.accounts) + 1)

    def get_full_name(self, account_number):
        account = self.find_account(account_number)
        return account.get_full_name()

    def get_accounts(self):
        return self.accounts

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        raise ValueError("Account couldn't be found")

    def deposit(self, amount, account_number):
        if amount > 0:
            account = self.find_account(account_number)
            account.deposit(amount)
            self.balance += amount

    def withdraw(self, amount, account_number, pin):
        if amount > 0:
            account = self.find_account(account_number)
            account.withdraw(amount, pin)
            self.balance -= amount

    def transfer(self, from_account_number, to_account_number, transfer_amount, from_pin, to_pin):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        amount_is_positive = transfer_amount > 0
        amount_in_bank = from_account.get_balance() >= transfer_amount
        correct_from_pin = from_pin == from_account.get_pin()
        correct_to_pin = to_pin == to_account.get_pin()

        if amount_is_positive and amount_in_bank and correct_from_pin and correct_to_pin:
            from_account.withdraw(transfer_amount, from_pin)
            to_account.deposit(transfer_amount)
