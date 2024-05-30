#!/usr/bin/python3
"""
This is the addition module.
it adds 2 integers
a and b must be first casted
"""


def add_integer(a, b=98):
     """a and are integers
    Returns an integer: the addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
