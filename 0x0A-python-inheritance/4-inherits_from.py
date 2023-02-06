#!/usr/bin/python3
"""Module to define the inherits_from function"""


def inherits_from(obj, a_class):
    """Function to return True if the object is an
        inherited instance from the specified class
        otherwise False
    """
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
