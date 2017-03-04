arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
result1 = sum(arr) - max(arr)
result2 = sum(arr) - min(arr)
print(result1, result2)
