#!/usr/bin/python3
"""Python script that sends a request to the URL passed in and
displays the value of the 'X-Request-Id' variable which is found
in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
