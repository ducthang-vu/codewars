import unittest
from list_squared import list_squared, sum_of_squared_divs, find_divs


class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])

    def test_string2(self):
        self.assertEqual(list_squared(42, 250), [[42, 2500], [246, 84100]])

    def test_string3(self):
        self.assertEqual(list_squared(250, 500), [[287, 84100]])