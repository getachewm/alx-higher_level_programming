#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the body of the response.
Prints an error message if the HTTP status code is greater than or equal to 400.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.RequestException as e:
        print(f"Error code: {e.response.status_code}" if e.response else f"Error: {e}")
