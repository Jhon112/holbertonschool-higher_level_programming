#!/usr/bin/python3
"""
fetches data from starwars api
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://swapi.co/api/people/"
    params = {'search': sys.argv[1]}
    r = requests.get(url, params=params)
    json = r.json()
    print('Number of results: ', json['count'])
    for obj in json['results']:
        print(obj['name'])
