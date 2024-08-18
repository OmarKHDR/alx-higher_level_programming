#!/usr/bin/python3
""" echo commits_hestory | head """
import requests
import sys


if __name__ == '__main__':
    api = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"
    res = requests.get(api)
    res = res.json()
    if isinstance(res, list):
        length = len(res) - 10
        if length < 0:
            length = 0
        for commit in res[length:]:
            print(f"{commit['sha']}:", commit['commit']['author']['name'])
