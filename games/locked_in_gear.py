import math

n = int(input())
gears = list()
for i in range(n):
    x, y, r = [int(j) for j in input().split()]
    if i == 0:
        gears.append([x, y, r, 'CW'])
    else:
        gears.append([x, y, r])

for r in range(3):
    for i in range(len(gears)):
        for j in range(len(gears)):
            if i != j:
                centersDistance = math.sqrt(((gears[i][0]-gears[j][0])**2) + ((gears[i][1]-gears[j][1])**2))
                radiusDistance = gears[i][2] + gears[j][2]
                if centersDistance == radiusDistance:
                    if (
                        gears[i][len(gears[i])-1] == "CW" and gears[j][len(gears[j])-1] != 'CCW' or
                        gears[j][len(gears[j])-1] == "CW" and gears[i][len(gears[i])-1] != 'CCW'
                        ):
                        if gears[j][len(gears[j])-1] == "CW":
                            gears[i].append('CCW')
                        elif gears[i][len(gears[i])-1] == "CW":
                            gears[j].append('CCW')
                    elif (
                        gears[j][len(gears[j])-1] == "CCW" and gears[i][len(gears[i])-1] != 'CW' or
                        gears[i][len(gears[i])-1] == "CCW" and gears[j][len(gears[j])-1] != 'CW'
                        ):
                        if gears[j][len(gears[j])-1] == "CCW":
                            gears[i].append('CW')
                        elif gears[i][len(gears[i])-1] == "CCW":
                            gears[j].append('CW')

res = False
for i in range(len(gears)):
    if len(gears[i]) < 4:
        gears[i].append('NOT MOVING')
    if 'CW' in gears[i] and 'CCW' in gears[i]:
        res = True

if res:
    print('NOT MOVING')
else:
    print(gears[len(gears)-1][len(gears[len(gears)-1])-1])