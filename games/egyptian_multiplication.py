# Example
# a, b = 12, 3
# a, b = 7675, 179

# Input
a, b = [int(i) for i in input().split()]

# max is always x and min y
x, y = max(a, b), min(a, b)
toadd = ""

# verbose output
print(x, "*", y)
# loop until y is 0 (x*0 == 0)
while y > 0 :
    # if there's a remainder,
    # rest 1 to the multiplier value
    # and add the multiplied
    if (y % 2) == 1 :
            
        toadd = toadd + " + " + str(x)
        y -= 1
    
    # If not, double x 
    # and reduce by half
    elif (y % 2) == 0 :
        
        x *= 2
        y = int(y/2)
        
    # print each "operation"
    print("=", x, "*", str(y) + toadd)
        
# print the multiplication, 
# but it should be the same as evaluate the last printed "operation"
print("= " + str(a*b))
