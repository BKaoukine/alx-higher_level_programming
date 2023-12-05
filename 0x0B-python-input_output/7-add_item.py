#!/usr/bin/python3
"""Script."""
import json
import sys
module_name1 = '6_Load_from_json_file'
load_from_json_file = getattr(__import__(module_name1), 'load_from_json_file')
module_name2 = '5_save_to_json_file.py'
save_to_json_file = getattr(__import__(module_name1), 'save_to_json_file')

arguments = sys.argv[1:]

load_from_json_file(add_item.json)
save_to_json_file(arguments, add_item.json)
