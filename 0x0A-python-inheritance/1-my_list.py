#!/usr/bin/python3
"""Module to define a class that inherits from list
"""


class MyList(list):
    """A class named MyList"""

    def print_sorted(self):
        """Print the list sorted (ascending sort)"""
        print(sorted(self))
