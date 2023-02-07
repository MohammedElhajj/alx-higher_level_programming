#!/usr/bin/python3
"""Module to define the class_to_json function
"""


def class_to_json(obj):
    """Returns the dictionary description of an object

    Args:
        obj(object): the object to be descriped
    """
    return obj.__dict__
