#!/usr/bin/python3
""" echo commits_hestory | head """
import requests
import sys


if __name__ == '__main__':
    api = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"
    res = requests.get(api)
    res = res.json()
    i = 0
    for commit in res:
        if i < 10:
            print(f"{commit['sha']}:", commit['commit']['author']['name'])
            i+=1
        else:
            break
