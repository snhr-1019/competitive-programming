import sys

sys.setrecursionlimit(300000)

N = int(input())

e = [[] for i in range(N + 1)]

for i in range(N - 1):
    A, B = map(int, input().split())
    e[A].append(B)
    e[B].append(A)

for i in range(N + 1):
    e[i].sort()

ans = []


def dfs(curr, pre):
    ans.append(curr)
    for nxt in e[curr]:
        if nxt != pre:
            dfs(nxt, curr)
            ans.append(curr)


dfs(1, -1)
print(*ans)
