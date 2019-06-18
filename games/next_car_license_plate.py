# Input
# QS-456-DF
# 1000000
# Output 
# QT-457-PS

import string

# input license plate and number of cars registered after
x = input().split("-")
num = int(input())

# create letter structure from AA to ZZ
ltrs = string.ascii_uppercase
letters = [''.join([a,b]) for a in ltrs for b in ltrs]

# count number of times the number exceeds the max
# (999 number, 676 letters)
times = (num+int(x[1]))//999
# num - number of times it exceeds
# number to add to the number or position
out1 =  int(x[1]) + num - 999*times

# repeat with the other components
num2 = (letters.index(x[2])+times)
times2 = num2//len(letters)
out2 = letters[num2 - len(letters)*times2]

num3 = (letters.index(x[0])+times2)
times3 = num3//len(letters)
out3 = letters[num3 - len(letters)*times3]

# print with format
print(out3+"-"+format(out1, '03')+"-"+out2)
