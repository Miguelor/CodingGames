# =============================================================================
# Input
# 5
# 3
# C X X X C
# X X X X X
# X X X X X
# X X X X X
# C X X X C
# =============================================================================

import numpy as np

n = int(input())
l = int(input())

room_lights = np.zeros((n,n), dtype=int)

for i in range(n) :
    line = input().split()
    for j in range(len(line)) :
        if line[j] == "C" :
            up, down, left, right = l-1, l-1, l-1, l-1 
            
            if ( i - up ) < 0 :
                up = i
            
            if ( j - left ) < 0 :
                left = j
                
            if ( i + down ) >= n :
                down = n - i - 1
            
            if ( j + right ) >= n :
                right = n - j -1
            
            room_lights[i-up:i+down+1,j-left:j+right+1] = 1

print( np.count_nonzero(room_lights == 0) )