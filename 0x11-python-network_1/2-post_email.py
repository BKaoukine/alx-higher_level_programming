#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL.

and displays the value of the X-Request-Id.
variable found in the header of the response.
"""
from urllib import request, parse
import sys
if __name__ == "__main__":

    dic = {'email': sys.argv[2]}

    enc_data = parse.urlencode(dic).encode('ascii')
    url = sys.argv[1]

    with request.urlopen(url, data=enc_data) as respons:

        body = respons.read()

        print(body.decode('utf-8'))
