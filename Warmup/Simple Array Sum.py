import sys
# import platform
# print(platform.python_version())

n = int(str(input()).strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# arr = map(lambda x: int(x), input().strip().split(' '))
sum = 0
for i in range(n):
    sum += arr[i]

print(sum)

# n = int(input().strip())
# print(sum([int(arr_temp) for arr_temp in input().strip().split(' ')]))
