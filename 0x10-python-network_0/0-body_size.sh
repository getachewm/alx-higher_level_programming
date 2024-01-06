#!bin/bash
# Getting the bytes size of the HTTP response header fro a given URL.
curl -s "$1" | wc -c
