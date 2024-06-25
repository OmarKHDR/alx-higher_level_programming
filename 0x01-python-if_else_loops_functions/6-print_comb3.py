#!/usr/bin/python3
t=0
for i in range(t,10):
    for j in range(t+1,10):
        print("{0:d}{1:d}".format(i, j), end=(", ", "\n")[i == 8 and j == 9])
    else:
        t=t+1
