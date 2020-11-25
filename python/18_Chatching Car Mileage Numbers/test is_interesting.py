import unittest
from is_interesting import is_interesting, all_digit_equal, all_digit_0_but_first, increasing_digits, \
	decreasing_digits, is_palindrome, is_interesting_array, is_interesting_simple


class SequenceTest(unittest.TestCase):
	def test_string_98_noarray(self):
		self.assertEqual(is_interesting(98, [5, 10]), 1)

	def test_string_99_noarray(self):
		self.assertEqual(is_interesting(99, [5, 10]), 1)

	def test_string_98_witharray(self):
		self.assertEqual(is_interesting(98, [5, 100]), 1)

	def test_string_99_witharray(self):
		self.assertEqual(is_interesting(99, [5, 100]), 1)