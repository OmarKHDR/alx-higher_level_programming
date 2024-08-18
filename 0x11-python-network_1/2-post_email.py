#!/usr/bin/python3
"""this is document for post request with email"""
import urllib.request as req
import urllib.parse as parse
import sys


if __name__ == '__main__':
    mail = {
        'email': sys.argv[2]
    }
    dt = parse.urlencode(mail)
    dt = dt.encode('ascii')
    res = req.Request(sys.argv[1], data=dt)
    with req.urlopen(res) as f:
        r = f.read()
