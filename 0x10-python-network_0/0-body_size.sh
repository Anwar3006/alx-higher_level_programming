#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
if [ $# -lt 1 ]
then
    echo "No URL provided"
else
    curl -s "$1" | wc -c
fi