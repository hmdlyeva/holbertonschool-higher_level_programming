#!/usr/bin/python3
"""Defines JSON representation function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""

    return json.dumps(my_obj)
