# Input 
# C
# Output 
# 0 0 00 0000 0I

# Input and conver to binary with 7 digits
st = input()
binary = ''.join(format(ord(x), 'b').zfill(7) for x in st)

# split 0 and 1 in groups
sp_binary = list()
for i in range(len(binary)) :
    if i == 0 :
        numb = binary[i]
    else :
        new_numb = binary[i]
        if set(new_numb) == set(numb) :
            numb = numb + new_numb
        else :
            sp_binary.append(numb)
            numb = new_numb
    if i == len(binary)-1 :
        sp_binary.append(numb)

# check if 0 or 1 and count length
out = list()
for i in range(len(sp_binary)) :
    if set(sp_binary[i]) == set("1") :
        out.append("0")
    else :
        out.append("00")
    out.append("0"*(len(sp_binary[i])))
    
# print encoding
print(" ".join(out))
