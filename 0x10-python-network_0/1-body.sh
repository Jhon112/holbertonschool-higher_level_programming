#!/bin/bash
# takes in a URL, sends a GET request to the URL, displays the body of the response
curl -Lsf "$1"
