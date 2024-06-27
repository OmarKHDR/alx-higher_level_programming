#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print("{0:d} arguments{1:s}".format(argc, (':', '.')[argc == 0]))
    for i in range(0, argc):
        print("{}: {}".format(i+1, sys.argv[i + 1]))
