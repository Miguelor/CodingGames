
c = int(input())
candidates = dict()
keys = range(1, c+1)
for i in keys:
        candidates[i] = input()
        
v = int(input())
votes = list()
for i in range(v):
    votes.append(list(input().replace(" ", "")))

newCandidates = candidates.copy()
results = list()
for i in range(c):
    # SACAR CONTEOS
    counts = list()
    for j in range(v):
        counts.append(votes[j][0])
        counts.sort()
    counts = list(map(int, counts))
    # PERSONAS CON 0 VOTOS Y CONTEO DE VOTOS
    cnd  = list(set(newCandidates) - set(counts))
    cnd.sort()
    finalCount = [counts.count(l) for l in set(counts)]
    # SI HAY PERSONAS CON 0 VOTOS
    if len(cnd) > 0:
        results.append(newCandidates[cnd[0]])
        del newCandidates[cnd[0]]
        # QUITAR SUS VOTOS
        for j in range(v):
            votes[j][:] = (value for value in votes[j] if value != str(cnd[0]))
    # SI NO HAY PERSONAS CON 0 VOTOS
    else:
        # VER QUIEN TIENE MENOS VOTOS
        countRelation = dict((x,counts.count(x)) for x in set(counts))
        minVotes = min([k for k,v in countRelation.items() if (v) == min(finalCount)])
        if i == c-1: 
            results.append("winner:"+newCandidates[minVotes])
        else:
            results.append(newCandidates[minVotes])

        del newCandidates[minVotes]
        # QUITAR SUS VOTOS
        for j in range(v):
            votes[j][:] = (value for value in votes[j] if value != str(minVotes))

for i in range(c):
    print(results[i])