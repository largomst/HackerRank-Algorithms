n, k = input().strip().split()
n, k = int(n), int(k)
arr = [int(a) for a in input().strip().split(' ')]

arr_max = max(arr)
result = 0
if k < arr_max:
    result = arr_max - k
    print(result)
else:
    print(result)
