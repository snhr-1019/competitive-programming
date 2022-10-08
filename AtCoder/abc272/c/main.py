n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

odds = []
evens = []
for a in A:
    if len(odds) >= 2 and len(evens) >= 2:
        break
    if a % 2 == 0:
        evens.append(a)
    else:
        odds.append(a)

cands = [-1]
if len(odds) >= 2:
    cands.append(odds[0] + odds[1])
if len(evens) >= 2:
    cands.append(evens[0] + evens[1])

print(max(cands))
