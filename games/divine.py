# Example
# board = np.array([[4, 4, 1, 5, 1, 2, 5, 5, 1],
#                   [1, 4, 2, 1, 1, 2, 2, 4, 5],
#                   [1, 1, 5, 4, 5, 4, 4, 5, 1],
#                   [3, 2, 1, 3, 1, 3, 3, 1, 2],
#                   [1, 5, 3, 3, 5, 5, 2, 5, 2],
#                   [1, 1, 5, 5, 3, 5, 2, 3, 1],
#                   [2, 2, 5, 5, 4, 4, 3, 1, 3],
#                   [1, 4, 4, 3, 4, 1, 5, 5, 4],
#                   [3, 4, 1, 5, 5, 4, 1, 2, 5]], dtype = int)

#   V: Value, C: Check, M: Move?
# 1st check
#   0   0   C 
#   0   V   M 
#   0   0   C 
# 2nd check
#   0   0   0   0   0
#   0   V   M   C   C
#   0   0   0   0   0
# 3rd check
#   0   0   C 
#   0   0   C 
#   0   V   M 
#   0   0   0 
# 4th check
#   0   0   0
#   0   V   M 
#   0   0   C 
#   0   0   C 

import numpy as np
import pandas as pd

# input and create board
boardNumbers = list()
for i in range(9):
    l = input().split(' ')
    boardNumbers.append(l)

board = np.array(boardNumbers, dtype=int)

# loop by columns and rows
moves = list()
for i in range(9):
    for j in range(9):
            value = board[i, j]
            # check right and left
            for y in (-1, 1):
                # check if the closest cell right and left exist
                if 0 <= i+y <= 8:
                    # no sense to exchange numbers if they are the equal
                    if value != board[i+y, j]:
                        # check if diagonals (for each direction) exist
                        # and append move if they are equal to the cell value 
                        if 0 <= j+1 <= 8 and 0 <= j-1 <= 8:
                            if value == board[i+y, j+1] and value == board[i+y, j-1]:
                                moves.append([i ,j, i+y, j])
                        # check if there are cells 2 and 3 positions ahead
                        # and append move if they are equal to the cell value
                        if 0 <= i+2*y <= 8 and 0 <= i+3*y <= 8:
                            if value == board[i+2*y, j] and value == board[i+3*y, j]:
                                moves.append([i, j, i+y, j])
                        # check diagonal and next value (non diagonal)
                        # and append move if they are equal to the cell value
                        if 0 <= j-2 <= 8:
                            if value == board[i+y, j-1] and value == board[i+y, j-2]: 
                                moves.append([i, j, i+y, j])
                        if 0 <= j+2 <= 8:
                            if value == board[i+y, j+1] and value == board[i+y, j+2]: 
                                moves.append([i, j, i+y, j])
            
            # follow the same process but up and down
            for x in (-1, 1):
                if 0 <= j+x <= 8:
                    if value != board[i, j+x]:
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

# reorder moves because it's needed to output first the lower values
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

# print output
print(len(df))
for i in range(len(df)):
    print(str(df.iloc[i][0]) + " " + str(df.iloc[i][1]) + " " + str(df.iloc[i][2]) + " " + str(df.iloc[i][3]))
    
