import unittest
from AccountPackage.Bank import Bank


class TestBank(unittest.TestCase):

    def test_register(self):
        bank = Bank()
        bank.register("Baba", "Solo", "1234")
        account = bank.get_accounts()[0]
        self.assertEqual("Baba Solo 1234", account.get_full_name())

    def test_deposit(self):
        bank = Bank()
        bank.register("Baba", "Solo", "1234")
        bank.deposit(1000, bank.get_accounts()[0].get_account_number())
        current_balance = bank.get_accounts()[0].get_balance()
        self.assertEqual(1000, current_balance)

    def test_withdraw(self):
        bank = Bank()
        bank.register("Baba", "Solo", "1234")
        account_number = bank.get_accounts()[0].get_account_number()
        bank.deposit(5000, account_number)
        current_balance = bank.get_balance(account_number)
        self.assertEqual(5000, current_balance)
        bank.withdraw(2000, account_number, "1234")
        new_balance = bank.get_balance(account_number)
        self.assertEqual(3000, new_balance)

    def test_bank_transfer(self):
        bank = Bank()
        bank.register("Baba", "Solo", "1234")
        bank.register("Messi", "Wa", "1431")
        from_account = bank.get_accounts()[0].get_account_number()
        to_account = bank.get_accounts()[1].get_account_number()
        bank.deposit(5000, from_account)
        bank.transfer(from_account, to_account, 2000, "1234", "1431")
        from_account_check_balance = bank.find_account(from_account).get_balance()
        to_account_check_balance = bank.find_account(to_account).get_balance()
        self.assertEqual(3000, from_account_check_balance)
        self.assertEqual(2000, to_account_check_balance)


if __name__ == "__main__":
    unittest.main()
