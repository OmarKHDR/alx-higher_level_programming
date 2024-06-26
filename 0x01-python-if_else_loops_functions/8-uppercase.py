#!/usr/bin/python3

def uppercase(str1):
    k = ord('a')-ord('A')
    a=ord('a')
    z=ord('z')
    for i in range(len(str1)):
        print("{0}".format((str1[i],chr(ord(str1[i])-k))[ord(str1[i]) >= a and ord(str1[i]) <= z]),end=("","\n")[i == len(str1) - 1])
uppercase("hello world!")