import sys

sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

d = ((1, 0), (0, 1))

cur = (0, 0)
appeared = set()
appeared.add(a[0][0])
ans = 0


def dfs(cur):
    global ans
    global appeared
    if cur[0] == h - 1 and cur[1] == w - 1:
        ans += 1
        return

    for di, dj in d:
        ni, nj = cur[0] + di, cur[1] + dj

        if 0 <= ni < h and 0 <= nj < w:
            if a[ni][nj] in appeared:
                continue
            appeared.add(a[ni][nj])
            dfs((ni, nj))
            appeared.remove(a[ni][nj])


dfs(cur)
print(ans)
