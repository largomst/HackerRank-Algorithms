#!/bin/python3

import sys

n = int(input().strip())

# fac = lambda n: 1 if n == 1 else n * fac(n)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(n))
