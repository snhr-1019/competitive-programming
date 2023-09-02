import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
d = [[-1] * n for _ in range(n)]

for i in range(n - 1):
    di = list(map(int, input().split()))
    for j in range(i + 1, n):
        d[i][j] = di[j - i - 1]

g = (n + 1) // 2
groups = [[] for _ in range(g)]

ans = 0


def dfs(i, s):
    # print(i, s)
    if i == n:
        global ans
        ans = max(ans, s)
        return

    for gi in range(g):
        if len(groups[gi]) >= 2:
            continue
        elif len(groups[gi]) > 0:
            groups[gi].append(i)
            dfs(i + 1, s + d[groups[gi][0]][i])
            groups[gi].pop()
        else:
            groups[gi].append(i)
            dfs(i + 1, s)
            groups[gi].pop()
            break


dfs(0, 0)
print(ans)
