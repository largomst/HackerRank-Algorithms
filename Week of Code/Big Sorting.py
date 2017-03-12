#!/bin/python3

import sys

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(int(unsorted_t))
# your code goes here

unsorted.sort()

for i in unsorted:
    print(i)
