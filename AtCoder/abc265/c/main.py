h, w = map(int, input().split())
g = [['#'] * (w + 2)]
for i in range(h):
    g.append(['#'] + list(input()) + ['#'])
g.append(['#'] * (w + 2))

visited = [[False] * (w + 2) for _ in range(h + 2)]
cur = [1, 1]
visited[1][1] = True
vec = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1],
}

while True:
    v = vec[g[cur[0]][cur[1]]]
    nxt = [cur[0] + v[0], cur[1] + v[1]]
    if g[nxt[0]][nxt[1]] == '#':
        print(*cur)
        exit()
    if visited[nxt[0]][nxt[1]]:
        print(-1)
        exit()
    visited[nxt[0]][nxt[1]] = True
    cur = nxt
