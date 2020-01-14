#!/usr/bin/python3
"""
catches errors
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r:
        print(r.text)
    else:
        print("Error code:", r.status_code)
