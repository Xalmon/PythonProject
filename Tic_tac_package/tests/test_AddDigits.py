import unittest
from new_task_fm.add_digits import AddDigits


class TestAddDigits(unittest.TestCase):
    def test_sum_digits(self):
        add_digit = AddDigits()
        self.assertEqual(add_digit.sum_digits("38"), 2)
        self.assertEqual(add_digit.sum_digits("12"), 3)
        self.assertEqual(add_digit.sum_digits("99"), 9)

    # def test_sum_digits_negative_value(self):
    #     add_digit = AddDigits()
    #     self.assertEqual(add_digit.sum_digits("-38"), 0)
    #     self.assertEqual(add_digit.sum_digits("-12"), 0)
    #     self.assertEqual(add_digit.sum_digits("-9"), 0)


if __name__ == '__main__':
    unittest.main()
    