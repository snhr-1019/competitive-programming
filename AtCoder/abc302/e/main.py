n, q = map(int, input().split())
ans = n
edges = [set() for _ in range(n)]

for _ in range(q):
    query = input().split()
    if query[0] == '1':
        u, v = int(query[1]) - 1, int(query[2]) - 1
        if len(edges[u]) == 0:
            ans -= 1
        if len(edges[v]) == 0:
            ans -= 1
        edges[u].add(v)
        edges[v].add(u)
    else:
        v = int(query[1]) - 1
        for u in edges[v]:
            if len(edges[u]) == 1:
                ans += 1
            edges[u].remove(v)
        if len(edges[v]) > 0:
            ans += 1
        edges[v] = set()
    print(ans)
