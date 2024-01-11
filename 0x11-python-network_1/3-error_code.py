#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints the HTTP status code.
"""

from urllib import request, error
import sys

def fetch_url_content(url):
    try:
        with request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except error.HTTPError as e:
        print("Error code:", e.code)
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    content = fetch_url_content(url)

    if content is not None:
        print(content)
