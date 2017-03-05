n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

kind_num = [0] * 101
for i in arr:
    kind_num[i] += 1
paris = 0
for i in kind_num:
    i2 = i
    while i2 > 1:
        i2 -= 2
        paris += 1

print(paris)
