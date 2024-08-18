#!/usr/bin/python3
"""doc suck"""

import urllib.request as reqlib
import sys



req = reqlib.Request(sys.argv[1])

with reqlib.urlopen(req) as ans :
    r = ans.headers['X-Request-Id']
    print(r)
