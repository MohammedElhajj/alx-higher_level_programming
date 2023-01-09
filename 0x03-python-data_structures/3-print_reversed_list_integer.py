#!/usr/bin/python3
# A function prints all integers of a list in reverse order

def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for idx in range(len(my_list)):
            print("{:d}".format(my_list[idx]))
