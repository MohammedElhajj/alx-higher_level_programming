#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """ A function to print  an integer with "{:d}".format()
    Args:
        value: the value to be printed
    Returns:
        True if value has been correctly printed otherwise returns
        False and prints in stderr: the error precede by Exception
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
