#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_positives(self):
        self.assertEqual(max_integer([1, 8, 3]), 8)

    def test_negatives(self):
        self.assertEqual(max_integer([-5, -8, -1, -3]), -1)

    def test_neg_pos(self):
        self.assertEqual(max_integer([-5, 8, -30, 16, 3, -40]), 16)

    def test_at_end(self):
        self.assertEqual(max_integer([20, 15, 21]), 21)

    def test_one_element(self):
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_strings(self):
        self.assertEqual(max_integer(["name", "have"]), "name")

    def test_chars(self):
        self.assertEqual(max_integer(['a', 'g', 'h', 'b']), 'h')


if __name__ == '__main__':
    unittest.main()
