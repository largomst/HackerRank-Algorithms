#!/bin/python3

import sys

s = input().strip()
count = 1
for char in s:
    if ord(char) < 97:
        count += 1

print(count)
