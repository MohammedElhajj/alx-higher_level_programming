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
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

