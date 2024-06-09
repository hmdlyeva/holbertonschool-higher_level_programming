#!/usr/bin/python3
"""Adds all arguments to a Python list, and then saves them to a file"""

import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argList = []
if os.path.exists("add_item.json"):
    argList = load_from_json_file("add_item.json")
save_to_json_file(argList + sys.argv[1:], "add_item.json")
