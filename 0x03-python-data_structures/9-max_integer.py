#!/usr/bin/python3

def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list"""
    # return None if list is empty
    if not my_list:
        return None

    big = min(my_list)
    for x in my_list:
        if x > big:
            big = x
    return big
