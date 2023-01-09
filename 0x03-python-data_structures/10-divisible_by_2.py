#!/usr/bin/python3
# A function to find all multiples of 2 in a list

def divisible_by_2(my_list=[]):
    even_list = []
    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            even_list.append(True)
        else:
            even_list.append(False)
    return (even_list)
