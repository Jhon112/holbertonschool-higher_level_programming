#!/usr/bin/python3
"""
sends a POST request with letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://eb941b7447d3.43.hbtn-cod.io:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}
    r = requests.post(url, data=payload)
    if r.json():
        msg = "[{}] {}".format(r.json()['id'], r.json()['name'])
    else:
        msg = 'No result'
    print(msg)
