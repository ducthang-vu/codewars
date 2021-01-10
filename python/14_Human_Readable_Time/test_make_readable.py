import unittest
from make_readable import make_readable


class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(make_readable(0), "00:00:00")

    def test_string2(self):
        self.assertEqual(make_readable(5), "00:00:05")

    def test_string3(self):
        self.assertEqual(make_readable(60), "00:01:00")

    def test_string4(self):
        self.assertEqual(make_readable(86399), "23:59:59")

    def test_string5(self):
        self.assertEqual(make_readable(359999), "99:59:59")
