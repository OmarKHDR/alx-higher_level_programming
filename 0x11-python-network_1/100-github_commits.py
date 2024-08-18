#!/usr/bin/python3
""" echo commits_hestory | head """
import requests
import sys


if __name__ == '__main__':
    api = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"
    res = requests.get(api)
    res = res.json()
    for i in range(10):
        print(res[i]['sha'],f": {res[i]['commit']['author']['name']}")
