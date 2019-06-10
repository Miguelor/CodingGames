
# Input candidates
c = int(input())
candidates = dict()
keys = range(1, c+1)
for i in keys:
        candidates[i] = input()

# Input votes
v = int(input())
votes = list()
for i in range(v):
    votes.append(list(input().replace(" ", "")))

newCandidates = candidates.copy()
results = list()
for i in range(c):
    # count votes
    counts = list()
    for j in range(v):
        counts.append(votes[j][0])
        counts.sort()
    counts = list(map(int, counts))
    # final vote counting adding candidates with 0 votes
    cnd  = list(set(newCandidates) - set(counts))
    cnd.sort()
    finalCount = [counts.count(l) for l in set(counts)]
    # remove candidates with 0 votes
    if len(cnd) > 0:
        results.append(newCandidates[cnd[0]])
        del newCandidates[cnd[0]]
        for j in range(v):
            votes[j][:] = (value for value in votes[j] if value != str(cnd[0]))
    # if there's no one with 0 votes
    else:
        # eliminate the less voted candidate or choose the winner
        countRelation = dict((x,counts.count(x)) for x in set(counts))
        minVotes = min([k for k,v in countRelation.items() if (v) == min(finalCount)])
        if i == c-1: 
            results.append("winner:"+newCandidates[minVotes])
        else:
            results.append(newCandidates[minVotes])

        del newCandidates[minVotes]
        for j in range(v):
            votes[j][:] = (value for value in votes[j] if value != str(minVotes))

# print candidates order and the winner with a tag 
for i in range(c):
    print(results[i])
