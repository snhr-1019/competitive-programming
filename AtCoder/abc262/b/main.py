n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

ans = 0
for a in range(n - 2):
    for b in range(a + 1, n - 1):
        for c in range(b + 1, n):
            if b in edges[a] and c in edges[b] and a in edges[c]:
                ans += 1
print(ans)
