import unittest
from generate_hashtag import generate_hashtag

class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(generate_hashtag(''), False, 'Expected an empty string to return False')

    def test_string2(self):
        self.assertEqual(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')

    def test_string3(self):
        self.assertEqual(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')

    def test_string4(self):
        self.assertEqual(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')

    def test_string5(self):
        self.assertEqual(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')

    def test_string6(self):
        self.assertEqual(generate_hashtag('codewars is nice'), '#CodewarsIsNice',
                           'Should capitalize first letters of words.')

    def test_string7(self):
        self.assertEqual(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice',
                       'Should capitalize all letters of words - all lower case but the first.')

    def test_string8(self):
        self.assertEqual(generate_hashtag('c i n'), '#CIN',
                       'Should capitalize first letters of words even when single letters.')

    def test_string9(self):
        self.assertEqual(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice',
                       'Should deal with unnecessary middle spaces.')

    def test_string10(self):
        self.assertEqual(generate_hashtag(
        'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
        oooooooooooooooooooooooooooooooooooooooooooooooooong Cat'),
                       False, 'Should return False if the final word is longer than 140 chars.')