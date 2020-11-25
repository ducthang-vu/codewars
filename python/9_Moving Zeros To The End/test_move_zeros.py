import unittest
from move_zeros import move_zeros


class SequenceTest(unittest.TestCase):
    def test_array1(self):
        self.assertEqual(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])

    def test_array2(self):
        self.assertEqual(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                           [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_array3(self):
        self.assertEqual(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                           ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_array4(self):
        self.assertEqual(
            move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]),
            ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_array5(self):
        self.assertEqual(move_zeros([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0])

    def test_array6(self):
        self.assertEqual(move_zeros(["a", "b"]), ["a", "b"])

    def test_array7(self):
        self.assertEqual(move_zeros(["a"]), ["a"])

    def test_array8(self):
        self.assertEqual(move_zeros([0, 0]), [0, 0])

    def test_array9(self):
        self.assertEqual(move_zeros([0]), [0])

    def test_array10(self):
        self.assertEqual(move_zeros([False]), [False])

    def test_array11(self):
        self.assertEqual(move_zeros([]), [])