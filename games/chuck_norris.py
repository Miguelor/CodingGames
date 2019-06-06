# =============================================================================
# input C
# output 0 0 00 0000 0 00
# =============================================================================

st = input()

binary = ''.join(format(ord(x), 'b').zfill(7) for x in st)

sp_binary = list()
for i in range(len(binary)) :
    print(i)
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

out = list()
for i in range(len(sp_binary)) :
    if set(sp_binary[i]) == set("1") :
        out.append("0")
    else :
        out.append("00")
    out.append("0"*(len(sp_binary[i])))
    
print(" ".join(out))