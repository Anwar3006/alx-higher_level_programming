#!/usr/bin/python3
"""Defines a JSON encoding function"""
import json as j


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.
    Args:
        my_obj (str): string object to be encoded
        
    Return
        JSON string representation of my_obj"""
    with open(filename, mode='w') as f:
        j.dump(my_obj, f)
