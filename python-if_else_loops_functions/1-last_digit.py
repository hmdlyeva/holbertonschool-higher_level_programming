#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number))
if number[-1:] > 5:
    print("{} and is greater than 5".format(number[-1:]))
elif number[-1:] == 0:
    print("{} and is 0".format(number[-1:]))
else:
    print("{} and is less than 6 and not 0".format(number[-1:]))
