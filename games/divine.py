# =============================================================================
# board = np.array([[4, 4, 1, 5, 1, 2, 5, 5, 1],
#                   [1, 4, 2, 1, 1, 2, 2, 4, 5],
#                   [1, 1, 5, 4, 5, 4, 4, 5, 1],
#                   [3, 2, 1, 3, 1, 3, 3, 1, 2],
#                   [1, 5, 3, 3, 5, 5, 2, 5, 2],
#                   [1, 1, 5, 5, 3, 5, 2, 3, 1],
#                   [2, 2, 5, 5, 4, 4, 3, 1, 3],
#                   [1, 4, 4, 3, 4, 1, 5, 5, 4],
#                   [3, 4, 1, 5, 5, 4, 1, 2, 5]], dtype = int)
# =============================================================================

import numpy as np
import pandas as pd

boardNumbers = list()
for i in range(9):
    l = input().split(' ')
    boardNumbers.append(l)

board = np.array(boardNumbers, dtype=int)

moves = list()
for i in range(9):
    for j in range(9):
            value = board[i, j]
            for y in (-1, 1):
                if 0 <= i+y <= 8:
                    if value != board[i+y, j] and (i+y) >= 0 and (i+y) <= 8:
                        if 0 <= j+1 <= 8 and 0 <= j-1 <= 8:
                            if value == board[i+y, j+1] and value == board[i+y, j-1]:
                                moves.append([i ,j, i+y, j])
                        if 0 <= i+2*y <= 8 and 0 <= i+3*y <= 8:
                            if value == board[i+2*y, j] and value == board[i+3*y, j]:
                                moves.append([i, j, i+y, j])
                        if 0 <= j-2 <= 8:
                            if value == board[i+y, j-1] and value == board[i+y, j-2]: 
                                moves.append([i, j, i+y, j])
                        if 0 <= j+2 <= 8:
                            if value == board[i+y, j+1] and value == board[i+y, j+2]: 
                                moves.append([i, j, i+y, j])
            for x in (-1, 1):
                if 0 <= j+x <= 8:
                    if value != board[i, j+x] and (j+x) >= 0 and (j+x) <= 8:
                        if 0 <= i+1 <= 8 and 0 <= i-1 <= 8:
                            if value == board[i+1, j+x] and value == board[i-1, j+x]:
                                moves.append([i ,j, i, j+x])
                        if 0 <= j+2*x <= 8 and 0 <= j+3*x <= 8:
                            if value == board[i, j+2*x] and value == board[i, j+3*x]:
                                moves.append([i, j, i, j+x])
                        if 0 <= i-2 <= 8:
                            if value == board[i-1, j+x] and value == board[i-2, j+x]: 
                                moves.append([i ,j, i, j+x])
                        if 0 <= i+2 <= 8:
                            if value == board[i+1, j+x] and value == board[i+2, j+x]: 
                                moves.append([i ,j, i, j+x])

reorderedMoves = list()
for m in range(len(moves)):
    if moves[m][0] + moves[m][1] > moves[m][2] + moves[m][3]:
        if [moves[m][2], moves[m][3], moves[m][0], moves[m][1]] not in reorderedMoves:
            reorderedMoves.append([moves[m][2], moves[m][3], moves[m][0], moves[m][1]])
    else:
        if [moves[m][0], moves[m][1], moves[m][2], moves[m][3]] not in reorderedMoves:
            reorderedMoves.append([moves[m][0], moves[m][1], moves[m][2], moves[m][3]])

df = pd.DataFrame(reorderedMoves)
df = df.sort_values([0, 1, 2, 3])

print(len(df))
for i in range(len(df)):
    print(str(df.iloc[i][0]) + " " + str(df.iloc[i][1]) + " " + str(df.iloc[i][2]) + " " + str(df.iloc[i][3]))
    
