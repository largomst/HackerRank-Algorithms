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

tagIndexOffset = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),
                  (1, -1))


def findInTheDirection(count, offset_row, offset_col, cur_row, cur_col,
                       chessboard, n):
    if (cur_col + offset_col < n) and (cur_row + offset_row < n) and (
            cur_col + offset_col >= 0) and (cur_row + offset_row >= 0) and (
                chessboard[cur_row + offset_row][cur_col + offset_col] != 'x'):
        count += 1
        findInTheDirection(count, offset_row, offset_col, cur_row, cur_col,
                           chessboard, n)
    else:
        return count


count = 0

cur_row = rQueen - 1
cur_col = cQueen - 1

for i in range(len(tagIndexOffset)):
    findInTheDirection(count, tagIndexOffset[i][0], tagIndexOffset[i][1],
                       cur_row, cur_row, chessboard, n)

print(count)
