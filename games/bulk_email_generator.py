# Example
# 3
# This is the (first|second|third) choice.
# This is the (first|second|third) choice.
# This is the (first|second|third) choice.
#
# Example Output
# This is the first choice.
# This is the second choice.
# This is the third choice.
#
# Example
# 7
# (No choice)
# (Empty choice|)
# Lotsa (1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|100) choices
# Does it (wrap|unwrap)?
# (Multi
# line|Multi
# line)
# 
# Example Output
# No choice
# 
# Lotsa 3 choices
# Does it unwrap?
# Multi
# line

# Input
n = int(input())
text = list()
for i in range(n) :
    line = list(input())
    for j in range(len(line)) :
        text.append(line[j])
    if i != n-1 :
        text.append("\n")
    
choices = [i for i, char in enumerate(text) if char == "("], [i for i, char in enumerate(text) if char == ")"]
selections = list()

i = 0
for c in range(len(choices[1])) :
    sel = "".join(text[choices[0][c]+1:choices[1][c]]).split("|")
    
    ind = i
    while ind > len(sel)-1 :
        ind = abs(ind - len(sel))
    
    selections.append(sel[ind])
    i += 1

for s in range(len(selections), 0, -1) :
    s = s-1
    text[choices[0][s]] = selections[s]
    del text[choices[0][s]+1:choices[1][s]+1]
        
print("".join(text))
