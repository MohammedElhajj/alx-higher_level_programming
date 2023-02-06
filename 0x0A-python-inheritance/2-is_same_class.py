#!/usr/bin/python3
"""Module to define is_same_class function"""


def is_same_class(obj, a_class):
    """Function to return True if the object is exactly
        an instance of the specified class otherwise False
    """
    return type(obj) == a_class
