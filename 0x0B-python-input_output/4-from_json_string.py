#!/usr/bin/python3
"""Defines a JSON decoding function"""
import json as j


def to_json_string(my_obj):
    """DeSerialization of parameter to normal string representation
    Args:
        my_obj (str): JSON string object to be decoded

    Return
        Normal string representation of my_obj"""
    return j.loads(my_obj)
