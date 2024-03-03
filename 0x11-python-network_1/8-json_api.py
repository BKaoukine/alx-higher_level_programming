#!/usr/bin/python3
"""Python script that takes in a letter, sends a POST to the URL.

and displays the bodey or the error.
"""

import requests
import sys

if __name__ == "__main__":
#Variables
    letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"

    if not sys.argv[1]:
        letter = ""
    
    dic = {"q" : letter}


    resp = requests.post(url, data=dic)

    if resp.json:
        print(resp.text)
    
    elif resp.json is None:
        print("No result")
    else:
        print("Not a valid JSON")
