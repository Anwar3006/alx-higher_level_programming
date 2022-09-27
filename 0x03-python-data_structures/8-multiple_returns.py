#!/usr/bin/python3

def multiple_returns(sentence):
    """Function that returns a tuple, length of string and first character."""
    if not sentence:
        return (0, None)

    first = sentence[0]
    tup = (len(sentence), first)
    return (tup[0], tup[1])
