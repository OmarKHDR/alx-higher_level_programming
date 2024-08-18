#!/usr/bin/python3
"""a shitty place called earth"""
import sys
import urllib.request
import urllib.error


if __name__ == '__main__':
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            r = response.read()
            print(r.decode('utf-8'))

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
