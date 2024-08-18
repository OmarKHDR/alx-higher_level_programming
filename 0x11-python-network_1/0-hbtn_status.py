#!/usr/bin/python3
"""parsing"""

import urllib.request as reqlib


req = reqlib.Request("https://alx-intranet.hbtn.io/status")
with reqlib.urlopen(req) as response:
    r = response.read()
    print("Body response:")
    print("\t- type:", type(r))
    print("\t- content:", r)
    print("\t- utf8 content:", r.decode('utf-8'))