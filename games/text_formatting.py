intext = input()

formatted = list()
for i, c in enumerate(intext):
    if c != " ":
        if i == 0:
            formatted.append(c.upper())
    
        else:
            if not ((formatted[len(formatted)-1] == ",") & (c == ",")) | ((formatted[len(formatted)-1] == ".") & (c == ".")):                
                
                if formatted[len(formatted)-1] in [",", ";"]:
                    formatted.append(" ")
                    formatted.append(c.lower())
                elif formatted[len(formatted)-1] in ["."]:
                    formatted.append(" ")
                    formatted.append(c.upper())
                elif formatted[len(formatted)-1] not in [" ", ","]:
                    formatted.append(c.lower())
                elif formatted[len(formatted)-1] in [" "]:
                    formatted.append(c.lower())
    if (i != len(intext)-1):
        if (c == " ") & (formatted[len(formatted)-1] not in [" ", ".", ";", ","]) & (intext[i+1] not in [" ", ".", ";", ","]):
            formatted.append(" ")

print("".join(formatted))
            
        


