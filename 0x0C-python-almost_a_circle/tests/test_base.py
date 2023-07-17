#!/usr/bin/python3
"""Defines unittests for base.py.
"""
import unittest
from base import Base


class test_base(unittest.TestCase):

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.id, b3.id - 2)

    def test_with_arg(self):
        b1 = Base(20)
        b2 = Base(10)
        self.assertNotEqual(b1.id, b2.id)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)
