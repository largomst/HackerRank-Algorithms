#!/bin/python3

import sys

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
i = 0
start = True
E = 100
while i != 0 or start:
    if start:
        i = (k + i) % n
        start = False
        continue
    E -= (c[i] + k) % n
    i = (k + i) % n

print(E)
