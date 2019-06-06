# =============================================================================
w = 4
h = 5
# word = "M@NH@TT@N"
word = "HI!"
dic = [[" #  ","##  "," ## ","##  ","### ","### "," ## ","# # ","### "," ## ","# # ","#   ","# # ","### "," #  ","##  "," #  ","##  "," ## ","### ","# # ","# # ","# # ","# # ","# # ","### ","### "],
       ["# # ","# # ","#   ","# # ","#   ","#   ","#   ","# # "," #  ","  # ","# # ","#   ","### ","# # ","# # ","# # ","# # ","# # ","#   "," #  ","# # ","# # ","# # ","# # ","# # ","  # ","  # "],
       ["### ","##  ","#   ","# # ","##  ","##  ","# # ","### "," #  ","  # ","##  ","#   ","### ","# # ","# # ","##  ","# # ","##  "," #  "," #  ","# # ","# # ","### "," #  "," #  "," #  "," ## "],
       ["# # ","# # ","#   ","# # ","#   ","#   ","# # ","# # "," #  ","# # ","# # ","#   ","# # ","# # ","# # ","#   "," ## ","# # ","  # "," #  ","# # ","# # ","### ","# # "," #  ","#   ","    "],
       ["# # ","##  "," ## ","##  ","### ","#   "," ## ","# # ","### "," #  ","# # ","### ","# # ","# # "," #  ","#   ","  # ","# # ","##  "," #  ","### "," #  ","# # ","# # "," #  ","### "," #  "]]
# =============================================================================

import string
import re

w = int(input())
h = int(input())
word = list(input().upper())

dic = list()
for i in range(h) :
    
    line = input()
    line = re.findall('.{1,'+str(w)+'}', line)
    
    if len(line) < 26 :
        line.append(" "*w)
    
    if len(line[len(line)-1]) != w :
        line[len(line)-1] = line[len(line)-1] + " " * (w - len(line[len(line)-1]))
    
    dic.append(line)
    
letters = list(string.ascii_uppercase)

outputOrder = list()
for l in word :
    if l not in letters :
        outputOrder.append(len(letters))
    else :
        outputOrder.append(letters.index(l))

output = list()
for i in range(len(outputOrder)):
    for j in range(h) :
        if i == 0 :
            output.append(dic[j][outputOrder[i]])
        else:
            output[j] = output[j] + dic[j][outputOrder[i]]

for o in output :
    print(o)
    