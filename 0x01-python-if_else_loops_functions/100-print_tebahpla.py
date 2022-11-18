#!/usr/bin/python3

for i in range(122, 96, -1):
    if (i % 2 == 0):
        n = i
    else:
        n = i - 32
    print("{:c}".format(n), end="")
