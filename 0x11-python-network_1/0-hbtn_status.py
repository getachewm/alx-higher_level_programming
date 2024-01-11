#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urlopen(url) as response:
        response_content = response.read()
        print("Body response:")
        print(f"\t- type: {type(response_content)}")
        print(f"\t- content: {response_content}")
        print(f"\t- utf8 content: {response_content.decode('utf-8')}")
