#!/usr/bin/python3
"""Defines a JSON decoding function"""
import json as j


def load_from_json_file(filename):
    """Function creates an Object from a “JSON file”
    Args:
        my_obj (str): JSON string object to be decoded

    Return
        Normal string representation of my_obj"""
    with open(filename, encoding='utf-8') as f:
        return j.load(f)
