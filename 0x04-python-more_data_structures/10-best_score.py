#!/usr/bin/python3

def best_score(a_dictionary):
    """Function that returns a key with the biggest integer value."""
    if a_dictionary is None:
        return None

    best = max(a_dictionary.values(), default=None)
    for k, v in a_dictionary.items():
        if v == best:
            return k
