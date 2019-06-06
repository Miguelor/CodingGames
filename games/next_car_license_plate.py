# =============================================================================
# QS-456-DF
# 1000000
# Sol: QT-457-PS
# =============================================================================

import string

x = input().split("-")
num = int(input())

ltrs = string.ascii_uppercase
letters = [''.join([a,b]) for a in ltrs for b in ltrs]

times = (num+int(x[1]))//999
out1 =  int(x[1]) + num - 999*times

pos2 = letters.index(x[2])
num2 = (pos2+times)
times2 = num2//len(letters)
out2 = letters[num2 - len(letters)*times2]

pos3 = letters.index(x[0])
num3 = (pos3+times2)
out3 = letters[num3]


print(out3+"-"+format(out1, '03')+"-"+out2)