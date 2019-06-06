import numpy as np

n = int(input())
square = np.zeros((n,n), dtype=int)

magic = "MAGIC"
for i in range(n):
    square[i] = list(map(int, input().split()))

if list(np.unique(square)) != list(range(1, n*n+1)):
    magic = "MUGGLE"

mValue = 0
for i in range(n):
    mValue = mValue + square[0][i]

if (np.trace(square) != mValue) | (np.trace(np.fliplr(square)) != mValue):
    magic = "MUGGLE"
 
if (sum(np.sum(square, axis = 0)) != mValue*n) | (sum(np.sum(square, axis = 1)) != mValue*n):
    magic = "MUGGLE"

print(magic)
