import sys

sys.setrecursionlimit(10 ** 9)

h, w = map(int, input().split())

s = [['z'] * (w + 2)]
for _ in range(h):
    s.append(['z'] + list(input()) + ['z'])
s.append(['z'] * (w + 2))

sn = 'snuke'

d = ((0, 1), (1, 0), (0, -1), (-1, 0))


def dfs(i, j, k):
    if visited[i][j] or s[i][j] != sn[k]:
        return

    if (i, j) == (h, w):
        print('Yes')
        exit()

    visited[i][j] = True
    for di, dj in d:
        dfs(i + di, j + dj, (k + 1) % len(sn))
    visited[i][j] = False


visited = [[False] * (w + 2) for _ in range(h + 2)]
dfs(1, 1, 0)
print("No")
