import sys

sys.setrecursionlimit(10 ** 7)

n, q = map(int, input().split())
edges = [[] for _ in range(n + 10)]
for i in range(q):
    l, r = map(int, input().split())
    r += 1
    edges[l].append(r)
    edges[r].append(l)


def search(cur):
    global visited
    if cur == n + 1:
        print("Yes")
        exit()

    for nxt in edges[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            search(nxt)


visited = [False] * (n + 10)
search(1)
print("No")
