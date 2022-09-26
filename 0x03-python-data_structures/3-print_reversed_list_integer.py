#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers of a list, in reverse order"""

    my_list = my_list[::-1]
    for element in my_list:
        print("{}".format(element))
