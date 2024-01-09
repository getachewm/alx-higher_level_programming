#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints: Error code: followed by the HTTP status code.
Uses only the packages urllib and sys.
"""

import sys
from urllib import request, error

def fetch_url(url):
    try:
        with request.urlopen(url) as response:
            return response.read().decode('utf-8')

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    content = fetch_url(url)
    print(content)
