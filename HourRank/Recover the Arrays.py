#!/bin/python3

n = int(input().strip())
file = [int(a) for a in input().strip().split(' ')]
i = 0
linCount = 0
while i < n:
    e = file[i]
    for j in range(e):
        i += 1
    i += 1
    linCount += 1

print(linCount)
