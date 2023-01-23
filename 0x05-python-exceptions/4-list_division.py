#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ A function to divide 2 lists element by element
    Args:
        my_list_1: the first list
        my_list_2: the second list
        list_length: the number of elements to be divided
    Returns:
        A new list (length = list_length) with all divisions
    """
    my_div_list = []
    for idx in range(list_length):
        try:
            div = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            my_div_list.append(div)
    return (my_div_list)
