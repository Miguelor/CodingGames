# Input
# 17 5
...#...#.#.#...#.
.#..#...#....#...
..........#......
..###...###..##..
#################
# Output
.................
.................
...##...###..#...
.####..#####.###.
#################

import numpy as np

# Input
width, height = [int(i) for i in input().split()]
# create empty matrix
wall = np.zeros((height, width), dtype='|U16')
# input each "wall" line
for i in range(height):
    wall[i] = list(input())
# replace columns with ordered columns so we have all # grouped
for i in range(width):
    wall[:,i] = sorted(wall[:,i], reverse=True)
# print it
for i in range(height):
    print("".join(map(str,wall[i])))
