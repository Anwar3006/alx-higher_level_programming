#!/usr/bin/python3

def multiple_returns(sentence):
    """Function that returns a tuple with the length of a string and its first character."""
    if not sentence:
        return (0, None)
    else:
        first = sentence[0]
    tup = (len(sentence), first)

    return (tup[0], tup[1])
