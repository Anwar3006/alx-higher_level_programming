#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Function that prints a dictionary by ordered keys."""
    sort_d = sorted(a_dictionary.items())

    for k, v in sort_d:
        print('{0}: {1}'.format(k, v))
