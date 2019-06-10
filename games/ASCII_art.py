# Example
# w = 4
# h = 5
# word = M@NH@TT@N
# dic = [[" #  ","##  "," ## ","##  ","### ","### "," ## ","# # ","### "," ## ","# # ","#   ","# # ","### "," #  ","##  "," #  ","##  "," ## ","### ","# # ","# # ","# # ","# # ","# # ","### ","### "],
#        ["# # ","# # ","#   ","# # ","#   ","#   ","#   ","# # "," #  ","  # ","# # ","#   ","### ","# # ","# # ","# # ","# # ","# # ","#   "," #  ","# # ","# # ","# # ","# # ","# # ","  # ","  # "],
#        ["### ","##  ","#   ","# # ","##  ","##  ","# # ","### "," #  ","  # ","##  ","#   ","### ","# # ","# # ","##  ","# # ","##  "," #  "," #  ","# # ","# # ","### "," #  "," #  "," #  "," ## "],
#        ["# # ","# # ","#   ","# # ","#   ","#   ","# # ","# # "," #  ","# # ","# # ","#   ","# # ","# # ","# # ","#   "," ## ","# # ","  # "," #  ","# # ","# # ","### ","# # "," #  ","#   ","    "],
#        ["# # ","##  "," ## ","##  ","### ","#   "," ## ","# # ","### "," #  ","# # ","### ","# # ","# # "," #  ","#   ","  # ","# # ","##  "," #  ","### "," #  ","# # ","# # "," #  ","### "," #  "]]

import string
import re

# Input vars
w = int(input())
h = int(input())
word = list(input().upper())

# Input "dictionary", split in letters
# keeping lengths
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

# check each letter in the word
# append the order if found and 
# 26 if not, to get "?"
outputOrder = list()
for l in word :
    if l not in letters :
        outputOrder.append(len(letters))
    else :
        outputOrder.append(letters.index(l))

# create the output by looking up the index in the dictionary
output = list()
for i in range(len(outputOrder)):
    for j in range(h) :
        if i == 0 :
            output.append(dic[j][outputOrder[i]])
        else:
            output[j] = output[j] + dic[j][outputOrder[i]]

# print output line by line
for o in output :
    print(o)
    
