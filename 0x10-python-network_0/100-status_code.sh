#!/bin/bash
#fg;v;
curl -s -X GET $1 -o /dev/null/ -w "%{http_code}"
