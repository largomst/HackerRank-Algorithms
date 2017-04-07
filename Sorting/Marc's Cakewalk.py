#!/bin/python3

n = int(input().strip())
calories = sorted(list(map(int, input().strip().split(' '))), reverse=True)
print(sum([calories[i] * (2**i) for i in range(len(calories))]))
