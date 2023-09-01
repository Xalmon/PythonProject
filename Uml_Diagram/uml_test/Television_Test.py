import unittest
from Uml_Diagram.Television import TV


class TestTelevision(unittest.TestCase):

    def test_channel(self):
        tv = TV()
        tv.turn_on()
        self.assertEqual(tv.get_channel(), 1)
        tv.set_channel(5)
        self.assertEqual(tv.get_channel(), 5)
        tv.channel_up()
        self.assertEqual(tv.get_channel(), 6)
        tv.channel_down()
        self.assertEqual(tv.get_channel(), 5)
        tv.set_channel(105)
        self.assertNotEqual(tv.get_channel(), 100)
        tv.set_channel(100)
        self.assertEqual(tv.get_channel(), 100)

    def test_volume(self):
        tv = TV()
        tv.turn_on()
        self.assertEqual(tv.get_volume(), 50)
        tv.set_volume(5)
        self.assertEqual(tv.get_volume(), 5)
        tv.volume_up()
        self.assertEqual(tv.get_volume(), 6)
        tv.volume_down()
        self.assertEqual(tv.get_volume(), 5)
        tv.set_volume(105)
        self.assertNotEqual(tv.get_volume(), 105)
        tv.set_volume(100)
        self.assertEqual(tv.get_volume(), 100)
        tv.set_volume(-1)
        self.assertNotEqual(tv.get_volume(), 0)

    def test_on_and_off(self):
        tv = TV()
        self.assertFalse(tv.on)
        tv.turn_on()
        self.assertTrue(tv.on)
        tv.turn_off()
        self.assertFalse(tv.on)


