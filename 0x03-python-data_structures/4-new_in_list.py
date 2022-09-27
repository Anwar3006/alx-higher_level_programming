#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Function that replaces list element at a specific position(like in C)"""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
