# Example Input
# 9
# - 4 0 0 5 9 8 . 2
#
# Output
# -0.024589

# Input
n = int(input())
inp = list(input().split())

# no need to order if there are only 0s
nonZero = False
numbers = list(range(1,10))
for n in numbers:
    print(n)
    if str(n) in inp:
        nonZero = True


if nonZero == True:
    # different approach if there's a "-"
    if "-" in inp:
        # sort and relocate the dot after the first digit
        inp.sort()
        if "." in inp:
            inp.remove(".")
            inp.insert(2, ".")
    
    else:
        # reverse sort and relocate the dot at the end
        # or before a 0 if possible
        inp.sort(reverse = True)
        
        if ("." in inp) & ("0" not in inp):
            inp.remove(".")
            inp.insert(len(inp)-1, ".")
        elif ("." in inp) & ("0" in inp):
            inp.remove(".")
            inp.pop(len(inp)-1)
else:
    inp = "0"

# print output
print("".join(inp))
