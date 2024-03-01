#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as respons:

    body = respons.read()

    print("Body response:")
    print("\t- type: " + str(type(body)))
    print("\t- content: " + str(body))
    print("\t- utf8 content: " + str(body.decode("utf-8")))
