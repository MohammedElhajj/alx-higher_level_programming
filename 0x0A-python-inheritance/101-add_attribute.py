#!/usr/bin/python3
"""A module defines a function to adds a new attribute
    to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """Addition function

    Args:
        obj: the object
        name: the name of the attributes
        value: the value of the attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
