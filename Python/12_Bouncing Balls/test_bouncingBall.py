import unittest
from bouncingBall import bouncingBall


class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(3, bouncingBall(3, 0.66, 1.5))
    def test_string2(self):
        self.assertEqual(15, bouncingBall(30, 0.66, 1.5))
    def test_string3(self):
        self.assertEqual(1, bouncingBall(3, 0.5, 1.5))