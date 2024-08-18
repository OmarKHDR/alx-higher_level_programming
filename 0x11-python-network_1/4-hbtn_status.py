#!/usr/bin/python3
"""module docs"""
import requests


if __name__ == '__main__':
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    res = response.content.decode("utf-8")
    print("\t- type:", type(res))
    print("\t- content:", res)
