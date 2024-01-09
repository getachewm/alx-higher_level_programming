#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints: Error code: followed by the HTTP status code.
Uses only the packages urllib and sys.
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
