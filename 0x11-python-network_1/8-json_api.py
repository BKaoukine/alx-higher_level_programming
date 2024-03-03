#!/usr/bin/python3
"""Python script that takes in a letter, sends a POST to the URL.

and displays the bodey or the error.
"""

import requests
import sys

if __name__ == "__main__":
    # Variables:
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]

    dic = {"q": letter}
    # Code:

    resp = requests.post(url, data=dic)
    API_data = resp.json()
    if API_data:
        for key in API_data:
            print(f"[{API_data[key]}]")

    elif resp.status_code == 204:
        print("No result")
    else:
        print("Not a valid JSON")
