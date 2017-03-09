#!/bin/python3

import sys

d1, m1, y1 = input().strip().split(' ')
d1, m1, y1 = [int(d1), int(m1), int(y1)]
d2, m2, y2 = input().strip().split(' ')
d2, m2, y2 = [int(d2), int(m2), int(y2)]


def isLeapYear(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False


month = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if isLeapYear(y1):
    month[2] = 29

fine = 0

if y1 > y2:
    fine = 10000
elif y1 == y2:
    if m1 > m2:
        fine = (m1 - m2) * 500
    elif m1 == m2:
        if d1 > d2:
            fine = (d1 - d2) * 15
        else:
            pass
    else:
        pass
else:
    pass

print(fine)
