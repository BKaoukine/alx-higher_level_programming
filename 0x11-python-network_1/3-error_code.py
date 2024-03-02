#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL.

and displays the value of the X-Request-Id.
variable found in the header of the response.
"""
from urllib import request, HTTPError
import sys
if __name__ == "__main__":

    url = sys.argv[1]

    with request.urlopen(url) as respons:
        try:
            body = respons.read()
            print(body.decode('utf-8'))
        except HTTPError as error:
            print(error.code)
