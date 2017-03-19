#!/bin/python3

import sys

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
calories.sort(reverse=True)
# your code goes here

result = 0
for i in range(n):
    result += calories[i] * 2**i

print(result)