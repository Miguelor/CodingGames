#5
#0306406152
#1145185215X
#9780306406157
#9780306406154
#978043551907X
#
#n = 5
#isbns = list(['0306406152', '1145185215X', '9780306406157', '9780306406154', '978043551907X'])

n = int(input())
isbns = list()
for i in range(n):
    isbns.append(input())

invalid = list()
for isbn in isbns :
    
    if "X" in isbn[:len(isbn)-1] :
        invalid.append(isbn)
        continue
    
    if len(isbn) == 10 :

        isbnSUM = 0
        for c, i in zip(list(isbn), range(10, 1, -1)) :
            isbnSUM += int(c) * i
        if isbn[9] == "X" :
            mod = 10
        else : 
            mod = int(isbn[9])
        if (isbnSUM + mod) % 11 :
            invalid.append(isbn)

    elif len(isbn) == 13 :

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

    else :
        invalid.append(isbn)

if len(invalid) > 0 :
    print(str(len(invalid)) + " invalid:")
    for i in invalid :
        print(i)