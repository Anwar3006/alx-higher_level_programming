#!/usr/bin/python3

def no_c(my_string):
    """Function that removes all characters c and C from a string."""
    new_string = []
    for x in my_string:
        if x != 'c' and x != 'C':
            new_string.append(x)
    return "".join(new_string)
