#!/bin/bash
# sends a request to that UR
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
