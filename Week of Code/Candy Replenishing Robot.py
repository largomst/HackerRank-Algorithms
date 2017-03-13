#!/bin/python3


n, t = input().strip().split(' ')
n, t = [int(n), int(t)]
c = list(map(int, input().strip().split(' ')))

rare = n
count = 0
for i in range(t - 1):
    rare = rare - c[i]
    if rare < 5:
        count += (n - rare)
        rare = n

print(count)
