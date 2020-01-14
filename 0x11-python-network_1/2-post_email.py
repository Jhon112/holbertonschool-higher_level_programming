#!/usr/bin/python3
"""
fetches information from a url passed as parameter
and post email
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(payload)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        r = response.read()
        print(r.decode("utf-8"))
