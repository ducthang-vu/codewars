import unittest
from perimeter import perimeter

class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(perimeter(1), 8)
        self.assertEqual(perimeter(5), 80)
        self.assertEqual(perimeter(7), 216)
