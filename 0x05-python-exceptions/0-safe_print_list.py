#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ A function to print x elements of a list

    Args:
        my_list: the list of the elements
        x: the number of elements to be printed
    
    Returns:
        The real number of elements printed.
    """
    real_num = 0 # counter
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            real_nu += 1
        except IndexError:
            break
    print("")
    return (real_num)
