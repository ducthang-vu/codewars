import unittest
from spin_words import spin_words


class SentenceTest (unittest.TestCase):
    def test_first_last_name(self):
        new_sentence = spin_words('Hey fellow warriors')
        self.assertEqual(new_sentence, 'Hey wollef sroirraw')
        new_sentence = spin_words('This is a test')
        self.assertEqual(new_sentence, 'This is a test')
        new_sentence = spin_words('This is another test')
        self.assertEqual(new_sentence, 'This is rehtona test')
