#!/usr/bin/python3
"""
catches errors
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            r = response.read()
            print(r.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
