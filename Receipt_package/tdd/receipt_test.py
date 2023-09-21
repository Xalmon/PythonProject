import unittest


class receipt_test(unittest.TestCase):
    def test_that_you_can_register(self):
        pass

    def test_that_you_can_setup(self):
        pass

    def test_that_you_can_print_receipt(self):
        pass

    def test_that_your_info_is_valid(self):
        pass

    def test_collect_user_info(self):
        input_data = [("Alice", "123 Main St", "555-123-4567", "alice@example.com"),
                      ("Bob", "456 Elm St", "555-987-6543", "bob@example.com")]
        self.assertIn(f"Name: {name}", printed_output)
        self.assertIn(f"Address: {address}", printed_output)
        self.assertIn(f"Telephone: {telephone}", printed_output)
        self.assertIn(f"Email: {email}", printed_output)
