#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            k = ord(str[i]) - 32
            j = chr(k)
        else:
            j = str[i]
        print("{}".format(j), end="")
    print("{}".format("\n"), end="")
