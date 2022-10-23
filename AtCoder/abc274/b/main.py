h, w = map(int, input().split())
c = []
for _ in range(h):
    c.append(list(input()))

ans = []
for j in range(w):
    cnt = 0
    for i in range(h):
        if c[i][j] == '#':
            cnt += 1
    ans.append(cnt)

print(*ans)
