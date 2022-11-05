n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(1, n + 1):
    l = len(edges[i])
    print(l, *(sorted(edges[i])))
