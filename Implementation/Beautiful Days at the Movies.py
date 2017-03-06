def rev(s):
    return s[::-1]


arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
count = 0

for x in range(arr[0], arr[1] + 1):
    if abs(x - int(rev(str(x)))) % arr[2] == 0:
        count += 1

print(count)
