#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digits = abs(number) % 10
if number < 0:
    digits = -digits
print("Last digit of {} is {} and is ".format(number, digits), end="")
if digits == 0:
    print("0")
elif digits > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
