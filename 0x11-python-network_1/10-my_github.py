#!/usr/bin/python3
""" docs sucks pls """

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    base = HTTPBasicAuth(sys.argv[1],sys.argv[2])
    res = requests.get(f"https://api.github.com/users/{sys.argv[1]}", auth=base)
        
    response = res.json()
    print(response['id'])
