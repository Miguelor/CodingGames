# Side 3 Input
# 3
# output
# print(".    * ")
# print("    ***")
# print("   *****")
# print("  *     *")
# print(" ***   ***")
# print("***** *****")

# side input
n = int(input())


lines = list()
# create a side n triangle, multiplying "*" to the level (starting at lvl 0)
# and adding blanks at the beggining to maintain the geometry
for i in range(n) :
    lines.append(str(" ")*(n*2-i-1) + "*"+"*"*(i*2))

# create 2 n sided triangles maintainin the geometry with blanks
for i, j in zip(reversed(range(n)), range(n)) :
    lines.append(" "*(i) + "*"+"*"*(j*2) + " "*(1+1*(i*2)) + "*"+"*"*(j*2))

# add 1 dot at the beggining because the problem ask for it
lines[0] = "." +lines[0][1:]

# print
for l in lines :
    print(l)
