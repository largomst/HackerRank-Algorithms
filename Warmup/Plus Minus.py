#!/usr/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
positive, negative, zero = 0, 0, 0
for i in range(n):
    if arr[i] > 0:
        positive += 1
    elif arr[i] == 0:
        zero += 1
    else:
        negative += 1

print('%.6f' % (positive / n))
print('%.6f' % (negative / n))
print('%.6f' % (zero / n))
