#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        ld = number % 10
        print(ld, end="")
        return ld
    else:
        s = str(number)
        m = s[-1:]
        i = int(m)
        print(i, end="")
        return i
