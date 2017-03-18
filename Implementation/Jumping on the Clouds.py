#!/bin/python3

import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

i = 0
count = 0

while i != len(c) - 1:
    if i + 2 <= len(c) - 1 and c[i + 2] != 1:
        i += 2
        count += 1
    elif i + 1 <= len(c) - 1:
        i += 1
        count += 1
    else:
        pass

print(count)
