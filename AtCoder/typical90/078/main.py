n, m = map(int, input().split())

e = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        e[a].append(b)
    else:
        e[b].append(a)

ans = 0
for i in range(n):
    if len(e[i]) == 1:
        ans += 1
print(ans)
