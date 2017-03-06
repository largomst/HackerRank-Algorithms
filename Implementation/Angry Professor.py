t = int(input().strip())
for t0 in range(t):
    n, k = input().strip().split(' ')
    n, k = int(n), int(k)
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

    # bigger than k is no and over, or is yes
    result = 'YES'
    arrived = 0
    for i in arr:
        if i <= 0:
            arrived += 1
        if arrived >= k:
            result = 'NO'
    print(result)