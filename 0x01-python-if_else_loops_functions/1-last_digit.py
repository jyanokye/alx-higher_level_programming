#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


if number >= 0:
    i = number % 10
elif number < 0:
    s = str(number)
    i = s[-1:]
    i = int(i) * -1



if i > 5:
    print(f"Last digit of {number} is {i} and is greater than 5")
elif i == 0:
    print(f"Last digit of {number} is {i} and is 0")
elif i < 6:
    print(f"Last digit of {number} is {i} and is less than 6 and not 0")
