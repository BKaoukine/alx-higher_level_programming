#!/usr/bin/python3
"""Script"""
import json
import sys
module_name1 = '6_Load_from_json_file'
load_from_json_file = getattr(__import__(module_name1), 'load_from_json_file')
module_name2 = '5_save_to_json_file.py'
save_to_json_file = getattr(__import__(module_name1), 'save_to_json_file')

arg_list = []
for arg in sys.argv:
    arg_list.append(arg)

save_to_json_file(arg_list, add_item.json)
load_from_json_file(add_item.json)
