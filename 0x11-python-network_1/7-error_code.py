#!/usr/bin/python3
"""
catches errors
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r = requests.get(url).raise_for_status()
        print(r.text)
    except requests.exceptions.RequestException as error:
        print("Error code:", error.response.status_code)
