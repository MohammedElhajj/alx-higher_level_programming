#!/usr/bin/python3
"""A module to create a class named Square"""


class Square:
    """A class named Square"""
    def __init__(self, size=0):
        """
        Args:
        size(int): the size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
