import sys
import math

r = int(input())
l = [0] * r
v = int(input())
for i in range(v):
    c, n = [int(j) for j in input().split()]
    vow = c - n
    seconds = pow(5, vow) * pow(10, n)
    l[l.index(min(l))] += seconds
  
print(max(l))