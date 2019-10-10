#!/usr/bin/python3
"""Test max_integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class to test max_integer function No attributes are needed
    but different methods for differents test cases are.

    """

    def test_empty_list(self):
        """
        checks that the max_integer function returns None in case list passed
        is empty.
        """

        self.assertIs(max_integer([]), None)

    def test_returns_correct_value(self):
        """
        Test if it returns the correct value (max integer of an int list
        """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """
        Test if it returns the correct value (max integer)
        on a list with negative numbers
        """

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
