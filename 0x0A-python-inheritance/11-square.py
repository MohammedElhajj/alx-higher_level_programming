#!/usr/bin/python3
"""Module to create a class named Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square inherits from Rectangle
    Attributes:
        size(int): the size of the Square
    """
    def __init__(self, size):
        """Initialize a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
