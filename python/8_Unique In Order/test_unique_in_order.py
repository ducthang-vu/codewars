import unittest
from unique_in_order import unique_in_order


class SequenceTest(unittest.TestCase):
    def test_talk1(self):
        sequence = ('AAAABBBCCDAABBB')
        self.assertEqual(unique_in_order(sequence), ['A', 'B', 'C', 'D', 'A', 'B'])

    def test_talk2(self):
        sequence = ('ABBCcAD')
        self.assertEqual(unique_in_order(sequence), ['A', 'B', 'C', 'c', 'A', 'D'])

    def test_talk3(self):
        sequence = [1,2,2,3,3]
        self.assertEqual(unique_in_order(sequence), [1, 2, 3])

    def test_talk_empty_string(self):
        sequence = ''
        self.assertEqual(unique_in_order(sequence), [])

    def test_talk_empty_list(self):
        sequence = []
        self.assertEqual(unique_in_order(sequence), [])
