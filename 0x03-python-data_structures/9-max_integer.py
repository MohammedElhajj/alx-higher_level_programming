#!/usr/bin/python3
# A function to find the biggest integer of a list

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    else:
        max_int = my_list[0]
        for idx in range(len(my_list)):
            if my_list[idx] > max_int:
                max_int = my_list[idx]
        return (max_int)
