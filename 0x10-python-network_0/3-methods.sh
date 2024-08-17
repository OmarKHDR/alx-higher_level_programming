#!/bin/bash
# -__=
curl -s -I $1 | grep 'Allow: ' | tr -d 'Allow: '
