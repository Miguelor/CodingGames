import math
import decimal
# get more decimal precision
decimal.getcontext().prec = 100

results = list()
k = int(input())
# loop over the inputs
for i in input().split():
    a = float(i)
    # reduce comparisons, starting at 2*a
    # proved that exponential is higher at least until j = 2*a 
    # for numbers between 1 and 10000
    j = int(2*a)
    # do the first iteration computation
    nExp = decimal.Decimal(j*math.log(decimal.Decimal(a)))
    nFac = decimal.Decimal(sum(math.log(i) for i in range(1,j+1)))
    # check unequality, append to resulst and stop trying
    # if we found a positive
    while True:
        if nExp < nFac:
            results.append(j)
            break
        else:
            # would be too slow to calculate exponential and factorial
            # each iteration (tried it), so whe add the new value to the last iteration.
            j += 1
            nExp = decimal.Decimal(nExp) + decimal.Decimal(math.log(a))
            nFac = nFac + decimal.Decimal(math.log(j))

# print all results
print(" ".join(map(str,results)))
