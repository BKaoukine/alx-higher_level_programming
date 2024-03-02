#!/usr/bin/python3
"""Write a Python script that takes in a URL.

sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""
import requests
import sys


url = sys.argv[1]

if __name__ == "__main__":
    req = requests.get(url)
    x_req_id = req.headers['X-Request-Id']
    print(x_req_id)
