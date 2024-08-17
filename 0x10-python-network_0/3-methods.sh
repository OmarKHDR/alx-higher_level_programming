#!/bin/bash
# -__=
curl -s -X GET 0.0.0.0:5000/route_4 -I | grep 'Allow: ' | sed "s/Allow: //"
