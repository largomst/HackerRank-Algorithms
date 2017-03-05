n, k = input().strip().split(' ')
n, k = int(n), int(k)
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pairs = [(i, j) for i in range(len(arr)) for j in range(len(arr))
         if (i < j) and ((arr[i] + arr[j]) % k == 0)]

print(len(pairs))
