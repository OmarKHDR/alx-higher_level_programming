#!/bin/bash
# -__=
sudo curl -s -I $1 | grep 'Allow: ' | tr -d 'Allow: '
