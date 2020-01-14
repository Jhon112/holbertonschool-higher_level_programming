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
    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json['id'], json['name']))
        else:
            print("No result")
    except ValueError as err:
        print('Not a valid JSON')
