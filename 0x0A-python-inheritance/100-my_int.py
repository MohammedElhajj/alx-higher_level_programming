#!/usr/bin/python3
"""Module to define a class named MyInt"""


class MyInt(int):
    """MyInt class that inherits from int"""
    def __eq__(self, value):
        """Invert the == operaor"""
        return int.__ne__(self, value)

    def __ne__(self, value):
        """Invert the != operator"""
        return int.__eq__(self, value)
