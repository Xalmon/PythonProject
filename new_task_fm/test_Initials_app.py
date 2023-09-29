import unittest

from new_task_fm.Initials_app import InitialsApp


class TestInitialsApp(unittest.TestCase):

    def test_split_string_method_on_single_word(self):
        initial_app = InitialsApp()
        input_data = "Solo"
        expected_output = "Solo"
        self.assertEqual(initial_app.split_string(input_data), expected_output)

    def test_split_string_method_on_multiple_words(self):
        app = InitialsApp()
        input_data = "Grace Chigoziem Femi Martins"
        expected_output = "G.C Martins"
        self.assertEqual(app.split_string(input_data), expected_output)


if __name__ == '__main__':
    unittest.main()


def test_that_you_can_calculate_int():
    assert False
