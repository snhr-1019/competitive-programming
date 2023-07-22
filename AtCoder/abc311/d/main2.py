from collections import deque

n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * m for _ in range(n)]
visited[1][1] = True
que = deque()
que.append((1, 1))

while que:
    i, j = que.popleft()
    for di, dj in d:
        ci = i
        cj = j
        while True:
            v = visited[ci][cj]
            visited[ci][cj] = True

            if s[ci + di][cj + dj] == '#':
                if not v:
                    que.append((ci, cj))
                break

            ci += di
            cj += dj

print(sum(sum(i) for i in visited))
