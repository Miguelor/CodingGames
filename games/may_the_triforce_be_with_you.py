# =============================================================================
# n = 3
# print(".    * ")
# print("    ***")
# print("   *****")
# print("  *     *")
# print(" ***   ***")
# print("***** *****")
# =============================================================================

n = int(input())

lines = list()
for i in range(n) :
    lines.append(str(" ")*(n*2-i-1) + "*"+"*"*(i*2))

for i, j in zip(reversed(range(n)), range(n)) :
    lines.append(" "*(i) + "*"+"*"*(j*2) + " "*(1+1*(i*2)) + "*"+"*"*(j*2))

lines[0] = "." +lines[0][1:]

for l in lines :
    print(l)