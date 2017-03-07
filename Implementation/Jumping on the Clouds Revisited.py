#!/bin/python3

import sys

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
i = 0
E = 100
start = True
while i != 0 or start:
    i = (i + k) % n
    E -= c[i] * 2 + 1
    start = False
print(E)
