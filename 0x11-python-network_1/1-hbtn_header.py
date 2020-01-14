#!/usr/bin/python3
"""
fetches information from a url passed as parameter
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        r = response
        print(r.headers['X-Request-Id'])
