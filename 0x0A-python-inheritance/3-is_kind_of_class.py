#!/usr/bin/python3
"""Module to define the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Function to return True if the object is an instance
        of a class that inherited from otherwise False
    """
    return isinstance(obj, a_class)
