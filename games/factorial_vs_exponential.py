import math
import decimal
decimal.getcontext().prec = 100

results = list()
k = int(input())
for i in input().split():
    a = float(i)
    j = int(2*a)
    nExp = decimal.Decimal(j*math.log(decimal.Decimal(a)))
    nFac = decimal.Decimal(sum(math.log(i) for i in range(1,j+1)))
    while True:
        if nExp < nFac:
            results.append(j)
            break
        else:
            j += 1
            nExp = decimal.Decimal(nExp) + decimal.Decimal(math.log(a))
            nFac = nFac + decimal.Decimal(math.log(j))
            
print(" ".join(map(str,results)))