#!/usr/bin/python3

k = ord('a') - ord('A')
# 26 letter will be printed
for i in range(ord('Z'), ord('A')-1, -1):
    if i % 2 != 0:
        print(chr(i), end='')
    else:
        print(chr(i+k), end='')
