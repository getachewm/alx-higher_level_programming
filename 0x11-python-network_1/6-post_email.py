#!/usr/bin/python3
"""
a python script that sends a POST request to the passed URL with the
email as a parameter, and finally displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data_req = requests.post(url, {"email": email})

    print(data_req.text)
