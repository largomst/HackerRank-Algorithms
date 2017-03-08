#!/bin/python3

import sys

s = input().strip()
t = input().strip()
k = int(input().strip())

s_length = len(s)
t_length = len(t)

n = min(s_length, t_length)
same_count = 0
for i in range(n):
    if s[i] == t[i]:
        same_count += 1
    else:
        break

rare_s = s_length - same_count
rare_t = t_length - same_count

if (rare_s + rare_t) <= k:
    # if (rare_s + rare_t) <= k and ((rare_s + rare_t) - k) % 2 == 0:
    print('Yes')
else:
    print('No')
