#!/usr/bin/python3
"""Defines reading function"""


def read_file(filename=""):
    """Read a text file and prints it to stdout"""

    with open(filename, "r", encoding="utf-8") as f:
        for txtLine in f:
            print(txtLine, end="")
