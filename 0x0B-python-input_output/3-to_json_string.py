#!/usr/bin/python3
"""Defines a JSON encoding function"""
import json as j


def to_json_string(my_obj):
    """Serialization of parameter to JSON string representation
    Args:
        my_obj (str): string object to be encoded
        
    Return
        JSON string representation of my_obj"""
    return (j.dumps(my_obj))
