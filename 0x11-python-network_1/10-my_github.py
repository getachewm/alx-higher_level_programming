#!/usr/bin/python3
"""
a python script that takes GitHub credentials
(username and password) and uses the GitHub API to display user's id
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]
    data_res = requests.get(url, auth=(user, passwd))

    try:
        data_json = data_res.json()
        print(data_json["id"])
    except Exception:
        print("None")
