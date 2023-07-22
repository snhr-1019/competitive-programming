import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')

import sys

sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]
visited[1][1] = True


def dfs(i, j):
    for k in range(4):
        ci = i
        cj = j
        while True:
            v = visited[ci][cj]
            visited[ci][cj] = True

            if s[ci + di[k]][cj + dj[k]] == '#':
                if not v:
                    dfs(ci, cj)
                break

            ci += di[k]
            cj += dj[k]


dfs(1, 1)

ans = 0
for i in range(n):
    for j in range(m):
        ans += visited[i][j]
print(ans)
