#!/bin/python3

import sys

n = int(input().strip())
score = list(map(int, input().strip().split(' ')))

max_score = score[0]
max_count = 0
for i in range(n):
    if score[i] > max_score:
        max_score = score[i]
        max_count += 1

min_score = score[0]
min_count = 0
for i in range(n):
    if score[i] < min_score:
        min_score = score[i]
        min_count += 1

print(max_count, min_count)
