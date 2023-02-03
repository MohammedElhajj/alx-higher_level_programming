#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)
    def test_one_element_list(self):
        """Test a list with only one element"""
        self.assertEqual(max_integer([8]), 8)
    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_identical_values_list(self):
        """Test a list of identical values"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
    def test_list_of_negatives(self):
        """Test a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)
    def test_strings_list(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
    def test_float_and_int(self):
        """Test a list of integers and floats numbers"""
        self.assertEqual(max_integer([-2.5, -3, 4, 4.5]), 4.5)
    def test_string(self):
        """Test a string to define the maximum char"""
        self.assertEqual(max_integer("Bob"), 'o')

if __name__ == '__main__':
    unittest.main()
