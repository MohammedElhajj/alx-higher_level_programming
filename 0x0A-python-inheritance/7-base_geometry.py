#!/usr/bin/python3
"""Module to create a class named BaseGeometry"""


class BaseGeometry:
    """A BaseGeometry class"""

    def area(self):
        """Not implemented - Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
