#!/usr/bin/python3
"""This module defines a function that that prints a name"""


def say_my_name(first_name, last_name=""):
    """A function to print a name

    Args:
        first_name(str): the first name
        last_name(str): the last name

    Returns:
        My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
