n = int(input())
input = list(input().split())

nonZero = False
numbers = list(range(1,10))
for n in numbers:
    if str(n) in input:
        nonZero = True

if nonZero == True:
    if "-" in input:
        input.sort()
    
        if "." in input:
            input.remove(".")
            input.insert(2, ".")
    
    else:
        input.sort(reverse = True)
        
        if ("." in input) & ("0" not in input):
            input.remove(".")
            input.insert(len(input)-1, ".")
        elif ("." in input) & ("0" in input):
            input.remove(".")
            input.pop(len(input)-1)
else:
    input = "0"

print("".join(input))
