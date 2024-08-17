#!/bin/bash
curl -s -X GET $1 -o /dev/null/ -w "%{http_code}"
