# =============================================================================
# #Triangle
# n = 3
# corners = [[0, 0], 
# [400, 0],
# [200, 200]]
# 
# m = 5
# shots = [[200, 100],
# [-34, 23],
# [75, 5],
# [175, 174],
# [175, 176]]
# =============================================================================

corners = list()
shots = list()
n = int(input())
for i in range(n):
    corner = input().split(' ')
    corners.append([int(corner[0]), int(corner[1])])
m = int(input())
for i in range(m):
    shot = input().split(' ')
    shots.append([int(shot[0]), int(shot[1])])

def lineFromPoints(P,Q): 
    a = Q[1] - P[1] 
    b = P[0] - Q[0]  
    c = a*P[0] + b*P[1]  
  
    return [a, b, c]

lines = list()
for i in range(n):
    if i+1 < n:
        lines.append(lineFromPoints(corners[i], corners[i+1]))
    else:
        lines.append(lineFromPoints(corners[i], corners[0]))
        
#evaluate shots
for i in range(m):
    
    ev  = list()
    for j in range(n):
        
        if j + 2 < len(corners):
            k = 2
        elif j + 2 == len(corners):
            k = -j
        elif j + 2 > len(corners):
            k = -j+1
        
        value = shots[i][0] * lines[j][0] + shots[i][1] * lines[j][1]
        checkValue = corners[j+k][0] * lines[j][0] + corners[j+k][1] * lines[j][1]
        
        if (
                (checkValue <= lines[j][2] and value <= lines[j][2]) or 
                (checkValue >= lines[j][2] and value >= lines[j][2])
            ):
            ev.append(1)
        else:
            ev.append(0)
    
    if sum(ev) == len(corners):
        print('hit')
    else:
        print('miss')