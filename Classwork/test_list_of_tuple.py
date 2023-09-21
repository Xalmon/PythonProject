import unittest


def add_numbers_in_list(a, b):
    return a + b


class TestAddNumbers(unittest.TestCase):

    def test_that_you_can_add_positive_numbers(self):
        result = add_numbers_in_list(3, 4)
        self.assertEqual(result, 7)

    def test_that_you_can_add_negative_numbers(self):
        result = add_numbers_in_list(-2, -5)
        self.assertEqual(result, -7)
