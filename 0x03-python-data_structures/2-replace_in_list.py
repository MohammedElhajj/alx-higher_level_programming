#!/usr/bin/python3
# A function to rplace an element of a list at
# a specific position

def replace_in_list(my_list, idx, element):
    if (idx < 0) or (idx > len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
