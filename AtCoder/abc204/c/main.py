import sys
sys.setrecursionlimit(200000)


N, M = map(int, input().split())

e = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    e[A].append(B)

ans = 0


def dfs(s, curr, pre, visited):
    global ans
    visited.add(curr)
    #print(s, curr)
    ans += 1
    for nxt in e[curr]:
        if nxt != pre and nxt not in visited:
            dfs(s, nxt, curr, visited)


for s in range(1, N + 1):
    dfs(s, s, -1, set())
print(ans)
