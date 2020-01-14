#!/usr/bin/python3
"""
fetches information from a url passed as parameter
and post email
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
