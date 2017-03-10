#!/bin/python3

import sys

y = int(input().strip())

# your code goes here


def isLeapYear(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False


day_of_the_programmer = 256

if isLeapYear(y):
    days = 244
else:
    days = 243

rare_days = day_of_the_programmer - days

print('%d.%02d.%d' % (rare_days, 9, y))
