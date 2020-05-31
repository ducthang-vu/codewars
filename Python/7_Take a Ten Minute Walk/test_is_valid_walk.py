import unittest
from is_valid_walk import is_valid_walk


class WalkTest (unittest.TestCase):
    def test_talk(self):
        walk = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']
        result = is_valid_walk(walk)
        self.assertEqual(result, True)
        walk = ['e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w']
        result = is_valid_walk(walk)
        self.assertEqual(result, True)
        walk = ['e', 'w', 'e', 'w', 'e', 'w', 'e', 'w']
        result = is_valid_walk(walk)
        self.assertEqual(result, False)
        walk = ['e', 'w', 's', 'n', 'e', 'w', 's', 'n']
        result = is_valid_walk(walk)
        self.assertEqual(result, False)
