from AccountPackage.Accounts import Account


class Bank:
    def __init__(self):
        self.accounts = []
        self.account_counter = 1

    def register(self, first_name, last_name, account_number):
        new_account = Account(first_name, last_name, account_number)
        self.accounts.append(new_account)

    def get_accounts(self):
        return self.accounts

    def deposit(self, amount, account_number):
        account = self.find_account(account_number)
        if account:
            account.balance += amount

    def withdraw(self, amount, account_number):
        account = self.find_account(account_number)
        if account and account.balance >= amount:
            account.balance -= amount

    def transfer(self, from_account_number, to_account_number, amount, from_account_pin, to_account_pin):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        if from_account and to_account and from_account.account_number != to_account.account_number:
            if from_account.account_number == from_account_pin and to_account.account_number == to_account_pin:
                if from_account.balance >= amount:
                    from_account.balance -= amount
                    to_account.balance += amount

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def generate_account_number(self):
        account_number = str(self.account_counter)
        self.account_counter += 1
        return account_number


if __name__ == "__main__":
    bank = Bank()

    bank.register("Baba", "Solo", "1234")
    bank.register("John", "Doe", "5678")

    bank.deposit(5000, "1")
    bank.transfer("1", "2", 2000, "1234", "5678")

    for account in bank.get_accounts():
        print(account.get_full_name(), account.get_balance())
