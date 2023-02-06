#!/usr/bin/python3
"""Module to create a class named Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square inherits from Rectangle
    Attributes:
        size(int): the size of the Square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
