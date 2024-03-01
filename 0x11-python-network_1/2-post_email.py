#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL.

and displays the value of the X-Request-Id.
variable found in the header of the response.
"""
from urllib import request, parse
import sys
if __name__ == "__main__":

    dic = {'email': sys.argv[2]}

    data = parse.urlencode(dic).encode
    url = sys.argv[1]

    with request.urlopen(url, data=data) as respons:

        body = respons.read()

        print(body.decode('utf-8'))
