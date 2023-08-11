#!/usr/bin/python3

import sys

elements = list(sys.argv)
length = len(elements)
j = 1

if length - 1 == 0:
    print("0 arguments.")
    exit()

print("{} arguments:".format(length - 1))
for i in elements[1:]:
    print("{:d}: {:s}".format(j, i))
    j += 1
