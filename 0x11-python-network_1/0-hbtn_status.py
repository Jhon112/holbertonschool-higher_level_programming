#!/usr/bin/python3
"""
fetches information from https://intranet.hbtn.io/status
"""
import urllib.request


with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    r = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(type(r), r, r.decode('utf-8'))
    )
