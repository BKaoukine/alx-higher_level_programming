#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as respons:

    body = respons.read()

    print("Body response:")
    print("- type: " + str(type(body)))
    print("- content: " + str(body))
    print("- utf8 content: " + str(body.decode("utf-8")))
