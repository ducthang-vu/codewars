import unittest
from is_pangram import is_pangram


class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(False, is_pangram('abcdefghijklmopqrstuvwxyz'))

    def test_string2(self):
        self.assertEqual(True, is_pangram('Cwm fjord bank glyphs vext quiz'))
