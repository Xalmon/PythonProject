import unittest
from test import area
from math import pi


class TestAreaFunction(unittest.TestCase):
    def test_area_function(self):
        self.assertAlmostEqual(area.area_check(1), pi)
        self.assertAlmostEqual(area.area_check(0), 0)
        self.assertAlmostEqual(area.area_check(2), pi * 2 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, area.area_check, -1)
        self.assertRaises(ValueError, area.area_check, -5)

    def test_radius_type(self):
        self.assertRaises(TypeError, area.area_check, True)
        self.assertRaises(TypeError, area.area_check, 2 + 5j)
