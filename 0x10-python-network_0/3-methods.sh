#!/bin/bash
# Takes in a URL and displays all HTTP methods the server
curl -is -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2-
