#!/usr/bin/python3
lower = range(97, 123)
upper = range(65, 91)


def uppercase(str):
    result = ""
    for i in str:
        if ord(i) in lower:
            i = chr(ord(i) - 32)
            result += i
        else:
            result += i
    print("{:s}".format(result), end="\n")
