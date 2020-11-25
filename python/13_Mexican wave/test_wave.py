import unittest
from wave import wave


class SequenceTest(unittest.TestCase):
    def test_string1(self):
        result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
        self.assertEqual(wave("hello"), result)

    def test_string2(self):
        result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
        self.assertEqual(wave("codewars"), result)

    def test_string3(self):
        result = []
        self.assertEqual(wave(""), result)

    def test_string4(self):
        result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs",
                  "two wordS"]
        self.assertEqual(wave("two words"), result)

    def test_string5(self):
        result = [" Gap ", " gAp ", " gaP "]
        self.assertEqual(wave(" gap "), result)