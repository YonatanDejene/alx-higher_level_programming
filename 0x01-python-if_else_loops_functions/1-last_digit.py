#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digits = abs(number) % 10
if digits > 5:
    print("Last digit of ", number, " is", digits," and is greater than 5")
elif digits < 6 and digits != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, digit))
else:
    print("0")
