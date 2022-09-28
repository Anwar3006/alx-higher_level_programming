#!/usr/bin/python3

def best_score(a_dictionary):
    """Function that returns a key with the biggest integer value."""
    if(a_dictionary):
        return (max(a_dictionary.keys()))
    else:
        return None
