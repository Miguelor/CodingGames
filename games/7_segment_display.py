#out = "1479"
#char = "#"
#num = 4

out = input()
char = input()
num = int(input())

blank = [" "*(num+2)]
horiz = [" " + char*num + " "]
vertone = [char + " "*(num+1)]*num
verttwo = [" "*(num+1) + char]*num
bothvert = [char + " "*(num) + char]*num

dic0 = list([horiz, bothvert, blank, bothvert, horiz])
dic0 = [item for dic0 in dic0 for item in dic0]

dic1 = list([blank, verttwo, blank, verttwo, blank])
dic1 = [item for dic1 in dic1 for item in dic1]

dic2 = list([horiz, verttwo, horiz, vertone, horiz])
dic2 = [item for dic2 in dic2 for item in dic2]

dic3 = list([horiz, verttwo, horiz, verttwo, horiz])
dic3 = [item for dic3 in dic3 for item in dic3]

dic4 = list([blank, bothvert, horiz, verttwo, blank])
dic4 = [item for dic4 in dic4 for item in dic4]

dic5 = list([horiz, vertone, horiz, verttwo, horiz])
dic5 = [item for dic5 in dic5 for item in dic5]

dic6 = list([horiz, vertone, horiz, bothvert, horiz])
dic6 = [item for dic6 in dic6 for item in dic6]

dic7 = list([horiz, verttwo, blank, verttwo, blank])
dic7 = [item for dic7 in dic7 for item in dic7]

dic8 = list([horiz, bothvert, horiz, bothvert, horiz])
dic8 = [item for dic8 in dic8 for item in dic8]

dic9 = list([horiz, bothvert, horiz, verttwo, horiz])
dic9 = [item for dic9 in dic9 for item in dic9]

dictionary = {"0":dic0, "1":dic1, "2":dic2, "3":dic3, "4":dic4, "5":dic5, "6":dic6, "7":dic7, "8":dic8, "9":dic9,}

outList = list([""]*len(dictionary["1"]))

for j in range(len(outList)) :
    for i in range(len(out)) :
        if i > 0 : 
            outList[j] = outList[j] + " " + dictionary[out[i]][j]
        else :
            outList[j] = outList[j] + dictionary[out[i]][j]

for i in range(len(outList)) :
    if char in outList[i] :
        clean = len(outList[i]) - outList[i][::-1].index(char)
        print(outList[i][:clean])
    else :
        print(outList[i])