#!/usr/bin/python3

import urllib.request as reqlib


req = reqlib.Request("https://alx-intranet.hbtn.io")

with reqlib.urlopen(req) as ans :
    r = ans.headers['X-Request-Id']
    print(r)
