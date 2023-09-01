import unittest

from Calculator import Calculator


class Calculator_test(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        expected = 5
        actual = calculator.add(2, 3)
        self.assertEqual(expected, actual)