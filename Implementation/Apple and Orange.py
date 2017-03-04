#!/bin/python3

import sys

s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

real_loc_of_apple = list()
real_loc_of_orange = list()

for item in apple:
    real_loc_of_apple.append(a + item)
for item in orange:
    real_loc_of_orange.append(b + item)

count_apple = 0
count_orange = 0

for a_apple in real_loc_of_apple:
    if a_apple in range(s, t + 1):
        count_apple += 1

for a_orange in real_loc_of_orange:
    if a_orange in range(s, t + 1):
        count_orange += 1

print(count_apple)
print(count_orange)
