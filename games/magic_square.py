import numpy as np

# input
n = int(input())
# create empty matrix
square = np.zeros((n,n), dtype=int)

# input numbers in the matrix
magic = "MAGIC"
for i in range(n):
    square[i] = list(map(int, input().split()))

# MUGGLE if not n*n unique numbers from 1 to max
if list(np.unique(square)) != list(range(1, n*n+1)):
    magic = "MUGGLE"

# calculate the "magic value"
mValue = 0
for i in range(n):
    mValue = mValue + square[0][i]
# diagonal and antidiagonal should be magic
if (np.trace(square) != mValue) | (np.trace(np.fliplr(square)) != mValue):
    magic = "MUGGLE"
 # same with rows and columns
if (sum(np.sum(square, axis = 0)) != mValue*n) | (sum(np.sum(square, axis = 1)) != mValue*n):
    magic = "MUGGLE"

# final trick
print(magic)
