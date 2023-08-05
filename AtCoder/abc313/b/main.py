n, m = map(int, input().split())
stronger = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    stronger[b].append(a)

cand = []
for i in range(n):
    if len(stronger[i]) == 0:
        cand.append(i)
if len(cand) == 1:
    print(cand[0] + 1)
else:
    print(-1)
