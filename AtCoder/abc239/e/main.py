import sys

sys.setrecursionlimit(10 ** 7)

n, q = map(int, input().split())
x = list(map(int, input().split()))
edges = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

values = [[] for _ in range(n)]
visited = [False for _ in range(n)]
visited[0] = True


def search(cur):
    global values
    ret = [x[cur]]
    for v in edges[cur]:
        if not visited[v]:
            visited[v] = True
            ret.extend(search(v))
    ret.sort(reverse=True)
    values[cur] = ret[:20]
    return values[cur]


search(0)

for i in range(q):
    v, k = map(int, input().split())
    v -= 1
    k -= 1
    print(values[v][k])
