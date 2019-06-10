# Example
# 0 0 00 00000 0 0 
# A

# Input encoding
enc = input().split(" ")
valid = True

# check pairs length < 2 (only 0 or 00) 
# check there's 7 digits
if any([len(e) > 2 for e in enc[::2]]) or sum([len(e) for e in enc[1::2]]) % 7 :
    valid = False

if valid :
    binary = ""
    
    # loop on pairs, add 1 if 0 and 0 if 00
    # multiply by the next odd length
    for i in range(0, len(enc), 2) :
        if len(enc[i]) == 1 :
            binary = binary + "1" * len(enc[i+1])
        else :
            binary = binary + "0" * len(enc[i+1])
    
    # split numbers in group of 7 (each one is a character)
    sp_binary = [(binary[i:i+7]) for i in range(0, len(binary), 7)]
    
    # add to output, transform base
    out = ""
    for  sp in sp_binary :
        out = out + chr(int(sp, 2))
    
    print(out)
else :
    print("INVALID")
