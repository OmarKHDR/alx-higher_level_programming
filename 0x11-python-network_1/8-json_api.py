#!/usr/bin/python3
""""gefeE"""
import requests
import sys


q = sys.argv[1] if len(sys.argv) > 1 else ""
res = requests.get("http://0.0.0.0:5000/search_user", data={'q':q})
try:
    dic = res.json()
    if dic:
        print(f"[{id}] {dic['id']}")
    else:
        print("No result")
except:
    print("Not a valid JSON")
