#!/usr/bin/python3
# A function to print all integers of a list

def print_list_integer(my_list=[]):
    for idx in range(len(my_list)):
        print("{:d}".format(my_list[idx]))
