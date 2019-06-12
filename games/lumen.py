# Input
# 5
# 3
# C X X X C
# X X X X X
# X X X X X
# X X X X X
# C X X X C

import numpy as np

# Input
n = int(input())
l = int(input())

# create empty matrix
room_lights = np.zeros((n,n), dtype=int)

# input lines with C (candle) and X (empty)
for i in range(n) :
    line = input().split()
    for j in range(len(line)) :
        
        # if a candles is found
        if line[j] == "C" :
            # mind the luminosity
            up, down, left, right = l-1, l-1, l-1, l-1 
            
            # checks to dont look outside the room
            if ( i - up ) < 0 :
                up = i
            
            if ( j - left ) < 0 :
                left = j
                
            if ( i + down ) >= n :
                down = n - i - 1
            
            if ( j + right ) >= n :
                right = n - j -1
            
            # replace all the iluminated area with 1s 
            room_lights[i-up:i+down+1,j-left:j+right+1] = 1

# print matrix
print( np.count_nonzero(room_lights == 0) )
