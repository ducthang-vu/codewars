import unittest
from decodeMorse import decodeMorse


class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual("HEY JUDE", decodeMorse('.... . -.--   .--- ..- -.. .'))