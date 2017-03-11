#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while arr != []:
    print(len(arr))
    min_of_arr = min(arr)
    for i in range(len(arr)):
        arr[i] -= min_of_arr
        if arr[i] < 0:
            a[i] = 0

    new_arr = [i for i in arr if i != 0]
    arr = new_arr
