#!/usr/bin/python3
"""This module defines a function that prints a square"""


def print_square(size):
    """A function to print a square using '#'

    Args:
        size(int): the size length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size > 0:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print()
