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

    def test_max_at_end(self):
        """
        Test if it returns the correct value (max integer of an int list
        """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beggining(self):
        """test if returns max value when it's at first position"""

        self.assertEqual(max_integer([4,3,2]), 4)

    def test_max_at_middle(self):
        """test if returns max value when it's at mid position"""

        self.assertEqual(max_integer([3, 2, 4, 1, 0]), 4)


    def test_unique_element(self):
        """Test list with only one element"""

        self.assertEqual(max_integer([4]), 4)

    def test_negative_numbers(self):
        """
        Test if it returns the correct value (max integer)
        on a list with negative numbers
        """

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
