#!/bin/python3

import sys

s = input().strip()
n = int(input().strip())
time = sum([1 for i in s if i == 'a']) * (n // len(s))
time += sum([1 for i in range(n % len(s)) if s[i] == 'a'])
print(time)
