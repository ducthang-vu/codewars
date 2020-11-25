import unittest
from scramble import scramble


class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(scramble('rkqodlw', 'world'), True)

    def test_string2(self):
        self.assertEqual(scramble('cedewaraaossoqqyt', 'codewars'), True)

    def test_string3(self):
        self.assertEqual(scramble('katas', 'steak'), False)

    def test_string4(self):
        self.assertEqual(scramble('scriptjava', 'javascript'), True)

    def test_string5(self):
        self.assertEqual(scramble('scriptingjava', 'javascript'), True)

    def test_string6(self):
        self.assertEqual(scramble('sermvihffsok', 'hizmdklesia'), False)

