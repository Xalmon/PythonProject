import unittest
from AccountPackage.Accounts import Account


class TestAccount(unittest.TestCase):

    def test_that_you_can_deposit(self):
        account = Account("Baba", "Solo", "1234")
        account.deposit(1000)
        self.assertEqual(1000, account.get_balance())

    def test_that_you_can_withdraw(self):
        account = Account("Baba", "Solo", "1234")
        account.deposit(1500)
        account.withdraw(1000, "1234")
        self.assertEqual(500, account.get_balance())

    def test_that_you_can_update_pin(self):
        account = Account("Baba", "Solo", "1234")
        account.update_pin("5678")
        self.assertEqual("5678", account.get_pin())

    def test_that_you_can_transfer(self, sender=None):
        account = Account("Baba", "Solo", "1234")
        sender.deposit(2000)

        recipient = Account("Alice", "Smith", "5678")
        recipient.deposit(1000)

        sender.transfer(1000, "1234", "5678")
        self.assertEqual(1000, sender.get_balance())
        self.assertEqual(2000, recipient.get_balance())

    def test_that_you_get_can_full_name(self):
        account = Account("Baba", "Solo", "1234")
        self.assertEqual("John Doe 1234", account.get_full_name())


if __name__ == '__main__':
    unittest.main()
