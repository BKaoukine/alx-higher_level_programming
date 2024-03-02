#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')

print("Body response:")
print("\t- type: " + str(type(r.text)))
print("\t- content: " + str(r.text))