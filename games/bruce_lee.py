#0 0 00 0000 0 0 

enc = input().split(" ")
valid = True

if any([len(e) > 2 for e in enc[::2]]) or sum([len(e) for e in enc[1::2]]) % 7 :
    valid = False

if valid :
    binary = ""
    for i in range(0, len(enc), 2) :
        if len(enc[i]) == 1 :
            binary = binary + "1" * len(enc[i+1])
        else :
            binary = binary + "0" * len(enc[i+1])
    
    sp_binary = [(binary[i:i+7]) for i in range(0, len(binary), 7)]
    
    out = ""
    for  sp in sp_binary :
        out = out + chr(int(sp, 2))
    
    print(out)
else :
    print("INVALID")