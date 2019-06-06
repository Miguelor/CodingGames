n = int(input())

glasses,levels = 0, 0 
for i in range(n) :
    if glasses+i >= n :
        break
    else : 
        levels += 1
        glasses += i+1

glass = [" ***  ",       
         " * *  ",  
         " * *  ",  
         "***** "]

if levels== 1 :
    for g in glass:
        print(g[:-1])
else :       
    for c in range(1, levels+1) :
        blanks = levels+1 - c
        for g in glass :
            print(str("   "*(blanks-1) + g*c +"   "*(blanks-1))[:-1])
