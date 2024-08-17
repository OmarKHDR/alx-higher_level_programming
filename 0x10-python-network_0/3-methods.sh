#!/bin/bash
# -__=
curl -s -X GET $1 -I | grep 'Allow: ' | sed "s/Allow: //"
