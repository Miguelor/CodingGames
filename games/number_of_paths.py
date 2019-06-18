# Examples
#
# m = 3
# n = 3
# board = np.matrix([[0, 0, 1],
#                    [1, 0, 0],
#                    [0, 0, 0]])
# 
# m = 10
# n = 10
# board = np.matrix([[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

import numpy as np

# input dimensions
m = int(input())
n = int(input())
# input board
board = np.zeros((m, n), int)
for i in range(m):
    row = input()
    board[i] = list(row)

# path going through first row
count = [[0 for x in range(m)] for y in range(n)] 
count[0][0] = 1
for i in range(1, m):
    if board[0, i] == 0:
        count[0][i] = count[0][i-1]

# path going through first column
for j in range(1, n):
    if board[j, 0] == 0:
        count[j][0] = count[j-1][0]

# adding the upper and left cells (only when there's no "wall" on the main 
# board), you get the different paths that can reach that particular cell, 
# a pattern of all possible paths is created and the last cell 
# has the final value
count = np.array(count)
for i in range(1, m):
    for j in range(1, n):
        if board[i, j] == 0:
            count[i, j] = count[i-1, j] + count[i, j-1]

# print last cell
print(count[-1, -1])
