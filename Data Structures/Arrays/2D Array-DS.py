arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

Y = len(arr[0])
X = len(arr)

value = [[0 for i in range(Y)] for i in range(X)]
# value 的边界不能全设置为 0，0 可能会成为最大值
# 另一种想法是找 value 的 max 时避开遍历边界

directions = [[-1, -1], [-1, 0], [-1, 1], [0, 0], [1, -1], [1, 0], [1, 1]]

for i in range(1, X - 1):
    for j in range(1, Y - 1):
        for direction in directions:
            value[i][j] += arr[i + direction[0]][j + direction[1]]

inf = float('inf')
max = -inf
for i in range(1, X - 1):
    for j in range(1, Y - 1):
        if value[i][j] > max:
            max = value[i][j]

print(max)
