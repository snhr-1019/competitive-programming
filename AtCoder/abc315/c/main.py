n = int(input())

t = [[] for _ in range(n)]
for _ in range(n):
    f, s = map(int, input().split())
    f -= 1
    t[f].append(-s)

for i in range(n):
    t[i].sort()

ans = 0
r = []
for i in range(n):
    if len(t[i]) >= 1:
        r.append(t[i][0])
    if len(t[i]) >= 2:
        ans = max(ans, -(t[i][0] + t[i][1] // 2))
r.sort()
if len(r) >= 2:
    ans = max(ans, -(r[0] + r[1]))
print(ans)
