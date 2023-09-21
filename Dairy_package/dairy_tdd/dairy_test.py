import unittest
from Dairy_package.Dairy import Diary


class TestDiary(unittest.TestCase):

    def setUp(self):
        self.dairy = Diary("hello", "good")
        self.dairy.create_entry("world", "mard")




