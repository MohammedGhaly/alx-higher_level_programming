#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Suite test of the function (max_integer function)"""

    def test_max_integer(self):
        self.assertEqual(max_integer([5, -5, 100, 7]), 100)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_repeated_number(self):
        self.assertEqual(max_integer([200, 200, 200]), 200)

    def test_float_numbers(self):
        self.assertEqual(max_integer([70, 71, 70, 69]), 71)

    def test_max_operated_integer(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12]), 25)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-10, -13, -9, -1]), -1)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([6, 5, 4, 3, 2, 1]), 6)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_big_list(self):
        self.assertEqual(max_integer([
            901, 902, 903, 904, 1000,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def test_list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 10 for i in my_list]), 50)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([2, '1'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([20, (30, 40)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key10': 10, 'key20': 20})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(20)
