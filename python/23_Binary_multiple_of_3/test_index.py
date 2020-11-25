import unittest
from index import PATTERN


class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(bool(PATTERN.match('0')), True)

    def test_string2(self):
        self.assertEqual(bool(PATTERN.match('abc')), False)

    def test_string3(self):
        self.assertEqual(bool(PATTERN.match('000')), True)

    def test_string4(self):
        self.assertEqual(bool(PATTERN.match('110')), True)

    def test_string5(self):
        self.assertEqual(bool(PATTERN.match('111')), False)

    def test_string6(self):
        self.assertEqual(bool(PATTERN.match('12345678')), True)

    def test_string6(self):
        self.assertEqual(bool(PATTERN.match('011')), True)
