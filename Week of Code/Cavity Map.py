#!/bin/python3

import sys

n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(grid_t)

matrix = [list(row) for row in grid]

for i in range(1, n - 1):
    for j in range(1, n - 1):
        if matrix[i][j - 1] < matrix[i][j] and matrix[i][j + 1] < matrix[i][
                j] and matrix[i - 1][j] < matrix[i][j] and matrix[i + 1][
                    j] < matrix[i][j]:
            matrix[i][j] = 'X'

for i in range(n):
    print(''.join(matrix[i]))