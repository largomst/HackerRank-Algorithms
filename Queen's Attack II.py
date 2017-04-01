#!/bin/python3

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]

chessboard = [[0] * n for i in range(n)]

rQueen, cQueen = input().strip().split(' ')
rQueen, cQueen = [int(rQueen), int(cQueen)]

chessboard[rQueen - 1][cQueen - 1] = 'Q'

for a0 in range(k):
    rObstacle, cObstacle = input().strip().split(' ')
    rObstacle, cObstacle = [int(rObstacle), int(cObstacle)]
    chessboard[rObstacle - 1][cObstacle - 1] = 'x'

tagIndexOffset = {{0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0},
                  {1, -1}}

for i in range(len(tagIndexOffset)):
    cur_row = x + tagIndexOffset[i][0]
    cur_col = y + tagIndexOffset[i][1]
    