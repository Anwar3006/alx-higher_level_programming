#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Function that replaces list element at a specific position (like in C)"""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    my_list[idx] = element
    return my_list
