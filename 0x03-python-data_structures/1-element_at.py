#!/usr/bin/python3

def element_at(my_list, idx):
    """Function that retrieves an element from a list like in C."""

    if idx < 0:
        return 0
    elif idx > len(my_list) - 1:
        return 0
    else:
        return (my_list[idx])
