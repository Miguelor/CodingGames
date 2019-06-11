# Examples
# 2*d6*d3-(3+d3)*d5>0
# 1+d4+1
# d9-2*d4

import re

# input and split
expr = input()
expresion = re.findall('[+-/*//()<>]|\w+', expr)

# add to the expresionsList
expresionsList = list()
expresionsList.append(expresion)

# multiply dices expresions "dx"
# remove expresion and add x new expresions with all the possible dice values
# repeat the process until there are no more "dx" expressions
for j in range(len(expresionsList[0])):
    if expresionsList[0][j].find('d') == 0:
        
        dice = int(re.findall(r'\d+', expresionsList[0][j])[0])
        lenEval = len(expresionsList)-1
        evaluated, i = False, 0
        while evaluated == False:
            expresionsToAdd = [''.join(expresionsList[i][0:(j)]) + str(k) + ''.join(expresion[(j+1):len(expresionsList[i])]) for k in range(1,(dice+1))]
            for l in expresionsToAdd:
                expresionsList.append(re.findall('[+-/*//()<>]|\w+', l))
            i += 1
            if i > lenEval:
                evaluated = True
        for k in range(lenEval+1):
            expresionsList.remove(expresionsList[0])

output = list()
# evaluate parenthesis and final expression
for ex in expresionsList:
    # replace parenthesis with 1, 0 or result
    for i in range(len(ex)):
        
        if ex[i].find('(') == 0:
            
            found, j = False, 1
            while found == False:
                if ex[i+j].find(')') == 0:
                    found = True
                else:
                    j += 1
            
            ev = eval(''.join(ex[i:i+j+1]))
            
            if ev == True:
                ev = 1
            elif ev == False:
                ev = 0
            
            # replace parenthesis, both numbers and sign with the evaluation
            ex[i], ex[i+1], ex[i+2], ex[i+3], ex[i+4] = '0', '0', str(ev), '.0', '0'
    
    # evaluate the expresion 
    finalEv = eval(''.join(ex))
    
    # if the final evaluation is a boolean, then make it 1 or 0
    if finalEv == True:
        finalEv = 1
    elif finalEv == False:
        finalEv = 0
            
    output.append(int(finalEv))
    
# get all unique results and count the repetitions
uniques = list(set(output))
uniques.sort()
counts = {x:output.count(x) for x in output}

# print unique results with their frequency
for i in range(len(uniques)):
    print(uniques[i], "%.2f" % round((counts[uniques[i]]/len(output))*100, 4))
