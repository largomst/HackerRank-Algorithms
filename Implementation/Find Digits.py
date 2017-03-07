#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = input().strip()

    n_list = list(n)
    count = 0
    for i in n_list:
        if int(i) == 0:
            continue
        if int(n) % int(i) == 0:
            count += 1
    print(count)
