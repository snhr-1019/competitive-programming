n = int(input())

a = []
for i in range(2 * n - 1):
    l = list(map(int, input().split()))
    a.append([0] * (i + 1) + l)

ans = 0


def dfs(dancers, score):
    if len(dancers) == 0:
        global ans
        ans = max(ans, score)
        return
    first = dancers[0]
    for i in range(1, len(dancers)):
        second = dancers[i]
        nxt_dancers = dancers[1:i] + dancers[i + 1:]
        dfs(nxt_dancers, score ^ a[first][second])


dfs(list(range(2 * n)), 0)
print(ans)
