#!/usr/bin/python3
"""Module to define a class named MyInt"""


class MyInt(int):
    """MyInt class that inherits from int"""
    def __equal__(self, value):
        """Invert the == operaor"""
        return int.__nequal__(self, value)

    def __nequal__(self, value):
        """Invert the != operator"""
        return int.__equal__(self, value)
