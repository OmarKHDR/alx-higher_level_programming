#!/usr/bin/python3
if __name__ == "__main__":
    import sys as sy
    s = 0
    for i in range(1, len(sy.argv)):
        num = int(sy.argv[i])
        s = s + num
    print("{:d}".format(s))
