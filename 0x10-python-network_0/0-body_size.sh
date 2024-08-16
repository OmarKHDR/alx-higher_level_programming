#!/bin/bash
url=$1
curl -s -X GET http://$1/ -H HTTP/1.0 -w "\n\n%{size_download}\n" | tail -n 1