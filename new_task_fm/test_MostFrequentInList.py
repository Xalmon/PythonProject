import unittest
from new_task_fm.MostFrequentInList import FrequentApp


class TestFrequentApp(unittest.TestCase):

    def test_the_empty_list(self):
        self.assertEqual(FrequentApp.most_frequent([]), [])

    def test_for_single_element_in_list(self):
        self.assertEqual(FrequentApp.most_frequent([5]), [5])

    def test_for_single_most_frequent_element_in_list(self):
        self.assertEqual(FrequentApp.most_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), [4])

    def test_for_multiple_most_frequent_elements_in_list(self):
        self.assertEqual(FrequentApp.most_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]), [4])

    def test_for_negative_numbers_in_list(self):
        self.assertEqual(FrequentApp.most_frequent([-1, -2, -2, -2, -3, -3, -3, -4, -4]), [-2, -3])


if __name__ == '__main__':
    unittest.main()
