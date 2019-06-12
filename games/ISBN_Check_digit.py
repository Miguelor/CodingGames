# Input
# 5
# 0306406152
# 1145185215X
# 9780306406157
# 9780306406154
# 978043551907X

# Input n and ISBNs
n = int(input())
isbns = list()
for i in range(n):
    isbns.append(input())

# loop over isbns
invalid = list()
for isbn in isbns :
    
    # input validations
    # no "X" until last position
    if "X" in isbn[:len(isbn)-1] :
        invalid.append(isbn)
        continue
    
    # if length 10
    if len(isbn) == 10 :
        
        # calculate isbn modulus
        # and append if invalid
        isbnSUM = 0
        for c, i in zip(list(isbn), range(10, 1, -1)) :
            isbnSUM += int(c) * i
        if isbn[9] == "X" :
            mod = 10
        else : 
            mod = int(isbn[9])
        if (isbnSUM + mod) % 11 :
            invalid.append(isbn)
    
    # if length 13
    elif len(isbn) == 13 :
        
        # calculate isbn modulus
        # and append if invalid
        isbnSUM = 0
        for c, i in zip(list(isbn), (1, 3)*6) :
            isbnSUM += int(c) * i
        if isbn[12] == "X" :
            invalid.append(isbn)
            continue
        else : 
            mod = int(isbn[12])
        if (isbnSUM + mod) % 10 :
            invalid.append(isbn)
    
    # if length not in 10,13
    # append to invalid
    else :
        invalid.append(isbn)

# print invalids ibns
if len(invalid) > 0 :
    print(str(len(invalid)) + " invalid:")
    for i in invalid :
        print(i)
