# Example
# 52+38=101

# Input
equality = input()

# Split in 3 terms 
x = equality.split("+",1)[0]
y = equality.split("=",1)[0].split("+",1)[1]
z = equality.split("=",1)[1]

# validation function
def val(c): 
    if c >= '0' and c <= '9': 
        return ord(c) - ord('0') 
    else: 
        return ord(c) - ord('A') + 10; 

# function to change base
def toDeci(str,base): 
    llen = len(str) 
    power = 1 #Initialize power of base 
    num = 0  #Initialize result  
    
    for i in range(llen - 1, -1, -1): 

        if val(str[i]) >= base: 
            #print('Invalid Number') 
            return -1
        num += val(str[i]) * power 
        power = power * base 
    return num 

# check from base 2 to 36
# make the base change and evaluate equivalence, print if true
for i in range(2, 37):
    basex, basey, basez = toDeci(x, i), toDeci(y, i), toDeci(z, i)
    if int(basex) + int(basey) == int(basez):
        print(i)
        break
