#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
m = abs(number) % 10 * -1 if number < 0 else number % 10

if m > 5:
    print("Last digit of %d is %d and is greater than 5" % (number, m))
elif m == 0:
    print("Last digit of %d is %d and is 0" % (number, m))
else:
    print("Last digit of %d is %d and is less than 6 and not 0" % (number, m))
