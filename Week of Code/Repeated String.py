#!/bin/python3

import sys

s = input().strip()
n = int(input().strip())
s = list(s)

a_time = 0
for i in s:
    if i == 'a':
        a_time += 1

s_length = len(s)
repeated_time = n // s_length
rare_s_index = n % s_length
rare_s = s[:rare_s_index]

a_rare_time = 0
for i in rare_s:
    if i == 'a':
        a_rare_time += 1

a_time = a_time * repeated_time + a_rare_time

print(a_time)
