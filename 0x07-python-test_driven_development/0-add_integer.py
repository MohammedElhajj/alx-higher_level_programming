#!/usr/bin/python3
"""This module defines a function that adds 2 integers"""


def add_integer(a, b=98):
    """A function to add two integers

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    if (type(a) != int or type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int or type(b) != float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

