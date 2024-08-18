#!/usr/bin/python3
"""doc sucks really"""

import urllib.request as reqlib
import sys


if __name__ == '__main__':
    req = reqlib.Request(sys.argv[1])
    with reqlib.urlopen(req) as ans :
        r = ans.headers['X-Request-Id']
        print(r)
