# Example 
# one,two,three.
#
# Output
# One, two, three.

# Input
intext = input()

# Create output list
formatted = list()

# loop over positions and characters
for i, c in enumerate(intext):
    
    # ignore blanks characters
    if c != " ":
        # uppercase first char
        if i == 0:
            formatted.append(c.upper())
    
        else:
            # don't add two equal punctuation marks
            if not (((formatted[len(formatted)-1] == ",") & (c == ",")) | 
                    ((formatted[len(formatted)-1] == ".") & (c == "."))):                
                
                # Add blanks after a ",", ";", "."
                # and append character (uppercase if following a dot)
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

    # adding blanks if necessary
    if (i != len(intext)-1):
        if ((c == " ") & 
            (formatted[len(formatted)-1] not in [" ", ".", ";", ","]) & 
            (intext[i+1] not in [" ", ".", ";", ","])):
            formatted.append(" ")

# print output
print("".join(formatted))
            
        


