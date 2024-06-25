#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    if i == ord('q') or i == ord('e'):
        continue
    print("{0:c}".format(i), end='')
