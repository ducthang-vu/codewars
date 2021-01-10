import unittest
from listPosition import listPosition


class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(listPosition('ABAB'), 2)

    def test_string2(self):
        self.assertEqual(listPosition('AAAB'), 1)

    def test_string3(self):
        self.assertEqual(listPosition('QUESTION'), 24572)

    def test_string4(self):
        self.assertEqual(listPosition('BOOKKEEPER'), 10743)

    def test_string5(self):
        self.assertEqual(listPosition('IMMUNOELECTROPHORETICALLY'), 78438425312655766989160)

    def test_string6(self):
        self.assertEqual(listPosition('UHUNTBEZPWFEQFUNKYZUIFNBK'), 821091853739268185699)
