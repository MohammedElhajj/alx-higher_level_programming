#!/usr/bin/python3
"""Module to define an object attribute lookup function
"""


def lookup(obj):
    """Function to return the list of available
    attributes of an object
    """
    return (dir(obj))
