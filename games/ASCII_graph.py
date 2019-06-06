# =============================================================================
# n = 0
# x, y = 1, 1
# points_x, points_y = list(), list()
# points_x.append(x)
# points_y.append(y)
# =============================================================================

import numpy as np

n = int(input())
points_x, points_y = list(), list()
for i in range(n):
    x, y = [int(j) for j in input().split()]
    points_x.append(x)
    points_y.append(y)

graph = np.array([[".", "|", "."],
                  ["-", "+", "-"],
                  [".", "|", "."]])

if n > 0 :

    column = np.array([["."],
                       ["-"],
                       ["."]])
    
    row = np.array([[".", "|", "."]])

    x_min, x_max = min(points_x), max(points_x)
    y_min, y_max = min(points_y), max(points_y)
    orig_x, orig_y =  1, 1

    if x_max > 0 :
        for i in range(x_max) :
            graph = np.append(graph, column, axis=1)
            row = np.append(row, np.array([["."]]), axis=1)
            
    if x_min < 0 :
        for i in range(abs(x_min)) :
            graph = np.append(column, graph, axis=1)
            row = np.append( np.array([["."]]), row, axis=1)
            orig_x += 1
            
    if y_max > 0 :
        for i in range(y_max) :
            graph = np.append(row, graph, axis=0)
            orig_y += 1
    
    if y_min < 0 :
        for i in range(abs(y_min)) :
            graph = np.append(graph, row, axis=0)
    
    for i in range(n) :
        graph[orig_y - points_y[i], orig_x + points_x[i]] = "*"
    
for g in graph :
    print("".join(list(g)))
