#!/usr/bin/python3
"""
fetches data from starwars api
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    usr = sys.argv[1]
    pwd = sys.argv[2]
    auth = requests.auth.HTTPBasicAuth(usr, pwd)
    r = requests.get(url, auth=auth)
    json = r.json()
    print(json.get('id'))
