#!/usr/bin/python3
"""module docs"""
import requests


if __name__ == '__main__':
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(response))
    print("\t- content:", response.content.decode("utf-8"))