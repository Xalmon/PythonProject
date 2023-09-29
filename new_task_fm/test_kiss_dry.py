import unittest
from new_task_fm.kiss_dry import KissDry


class TestKissDry(unittest.TestCase):

    def test_that_you_can_check_index(self):
        kiss_dry = KissDry()
        word = "kissdry"
        x = [6, 2, 3, 4, 1, 0, 5]
        expected_output = "yssdikr"
        self.assertEqual(kiss_dry.Check_index(word), expected_output)

