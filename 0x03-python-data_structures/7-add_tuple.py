#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds 2 tuples"""
    tuple_a  = tuple_len_check(tuple_a)
    tuple_b  = tuple_len_check(tuple_b)
    return (tuple_a[0] + tuple_b[0],tuple_a[1] + tuple_b[1])

 
def tuple_len_check(tuple_=()):
    """Function to check the lenght of the tuple"""
    if len(tuple_) < 2:
        if len(tuple_) == 1:
            tuple_ = [tuple_[0], 0]
        elif len(tuple_) == 0:
            tuple_ = (0, 0)
    elif len(tuple_) > 2:
            tuple_ = (tuple_[0], tuple_[1])
    return tuple_
