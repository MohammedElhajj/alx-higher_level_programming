#!/usr/bin/python3
def safe_print_division(a, b):
    """ A function to divide two integers and print the result
    Args:
        a: the first integer
        b: the second integer
    Returns:
        The value of a divided by  b.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
