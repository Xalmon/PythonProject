import unittest
from AccountPackage.Accounts import Account


class TestAccount(unittest.TestCase):

    def test_can_deposit_into_account(self):
        baba_account = Account("Baba", "Solo", "0000")
        current_balance = baba_account.get_balance()
        self.assertEqual(0, current_balance)
        baba_account.deposit(5000)
        current_balance = baba_account.get_balance()
        self.assertEqual(5000, current_balance)

    def test_negative_deposit_raises_exception(self):
        baba_account = Account("Baba", "Solo", "0000")
        current_balance = baba_account.get_balance()
        self.assertEqual(0, current_balance)

    def test_can_deposit_twice_account(self):
        baba_account = Account("Baba", "Solo", "0000")
        baba_account.deposit(8000)
        current_balance = baba_account.get_balance()
        self.assertEqual(8000, current_balance)
        baba_account.deposit(2000)
        new_balance = baba_account.get_balance()
        self.assertEqual(10000, new_balance)

    def test_cannot_deposit_negative_amount(self):
        baba_account = Account("Baba", "Solo", "0000")
        baba_account.deposit(1000)
        current_balance = baba_account.get_balance()
        self.assertEqual(1000, current_balance)
        baba_account.deposit(-2000)
        new_balance = baba_account.get_balance()
        self.assertEqual(1000, new_balance)

    def test_can_withdraw(self):
        baba_account = Account("Baba", "Solo", "0000")
        baba_account.deposit(5000)
        current_balance = baba_account.get_balance()
        self.assertEqual(5000, current_balance)
        baba_account.withdraw(2000, baba_account.get_pin())
        new_balance = baba_account.get_balance()
        self.assertEqual(3000, new_balance)

    def test_update_pin(self):
        baba_account = Account("Baba", "Solo", "0000")
        old_pin = baba_account.get_pin()
        baba_account.update_pin("newPin")
        new_pin = baba_account.get_pin()
        self.assertNotEqual(old_pin, new_pin)


if __name__ == "__main__":
    unittest.main()
