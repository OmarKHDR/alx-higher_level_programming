#!/usr/bin/python3

def uppercase(str1):
    k = ord('a')-ord('A')
    for i in range(len(str1)):
        print("{0}".format(chr(ord(str1[i])-k)),end=("","\n")[i == len(str1) - 1])

uppercase("hello")