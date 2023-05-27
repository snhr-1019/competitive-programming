n, m = map(int, input().split())
p = [[False] * n for _ in range(n)]

for i in range(m):
    a = list(map(int, input().split()))
    for j in range(n - 1):
        p[a[j] - 1][a[j + 1] - 1] = True
        p[a[j + 1] - 1][a[j] - 1] = True

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if not p[i][j]:
            ans += 1
print(ans)
