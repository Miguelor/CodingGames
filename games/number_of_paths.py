# =============================================================================
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
# =============================================================================

import numpy as np

m = int(input())
n = int(input())
board = np.zeros((m, n), int)
for i in range(m):
    row = input()
    board[i] = list(row)

count = [[0 for x in range(m)] for y in range(n)] 
count[0][0] = 1
for i in range(1, m):
    if board[0, i] == 0:
        count[0][i] = count[0][i-1]

for j in range(1, n):
    if board[j, 0] == 0:
        count[j][0] = count[j-1][0]

count = np.array(count)

for i in range(1, m):
    for j in range(1, n):
        if board[i, j] == 0:
            count[i, j] = count[i-1, j] + count[i, j-1]
            
print(count[-1, -1])
