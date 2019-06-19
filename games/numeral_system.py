# Example
# 52+38=101

equality = input()

x = equality.split("+",1)[0]
y = equality.split("=",1)[0].split("+",1)[1]
z = equality.split("=",1)[1]

def val(c): 
    if c >= '0' and c <= '9': 
        return ord(c) - ord('0') 
    else: 
        return ord(c) - ord('A') + 10; 

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

for i in range(2, 37):
    basex, basey, basez = toDeci(x, i), toDeci(y, i), toDeci(z, i)
    if int(basex) + int(basey) == int(basez):
        print(i)
        break
