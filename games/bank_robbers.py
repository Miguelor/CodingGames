import sys
import math

# Input
r = int(input())
l = [0] * r
v = int(input())
for i in range(v):
    # input characters, digits, and get vowels
    c, n = [int(j) for j in input().split()]
    vow = c - n
    # get max seconds, having in mind that 
    # there are 5 vowels and 10 digits
    seconds = pow(5, vow) * pow(10, n)
    # add to the output
    l[l.index(min(l))] += seconds
  
print(max(l))
