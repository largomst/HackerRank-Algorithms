#!/bin/python3

n = int(input().strip())
file = [int(a) for a in input().strip().split(' ')]
i = 0
linCount = 0
while i < n:
    # Skip 'i' past current array to the beginning of the next array
    i += file[i] + 1
    linCount += 1

print(linCount)
