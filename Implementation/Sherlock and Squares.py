import math
n = int(input().strip())
for i in range(n):
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    count = 0
    for a in range(arr[0], arr[1] + 1):
        a_sqrt = math.sqrt(a)
        if a_sqrt == int('%.0f' % a_sqrt):
            count += 1
    print(count)
