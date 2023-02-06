#!/usr/bin/python3
"""Module to create a class named Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class inherits from BaseGeometry
    Attributes:
        width: the width of the Rectangle
        height: the height of the rectangle
    """
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
