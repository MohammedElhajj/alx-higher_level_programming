#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ A function to print the first x integer elements
    Args:
        my_list: the list of the elements
        x: the number of elements to be printed
    Returns:
        The real number of elements printed.
    """
    real_num = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            real_num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (real_num)
