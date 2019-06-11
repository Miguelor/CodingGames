# Examples
# 8 5
# LEFT
#
# 9876542365445 5263442546547
# LEFT

import math 

# Input
n, s = [int(i) for i in input().split()]
d = input()

# Follow the solution
# https://en.wikipedia.org/wiki/Josephus_problem#Solution.
direction = 1 if d == 'LEFT' else -1
survivor = (s + direction * 2 * (n - math.pow(2,len(bin(n)[2:]) - 1))) % n
# Print
print(int(survivor))
