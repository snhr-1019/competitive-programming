n = int(input())
a = [list(input()) for _ in range(n)]

DIST = [(0, 1), (1, 0), (1, 1), (1, -1),
        (0, -1), (-1, 0), (-1, -1), (-1, 1)]

ans = 0
for i in range(n):
    for j in range(n):
        for d in DIST:
            ci = i
            cj = j
            num = [a[ci][cj]]
            for _ in range(n - 1):
                ci += d[0]
                ci %= n
                cj += d[1]
                cj %= n
                num.append(a[ci][cj])
            ans = max(ans, int("".join(num)))
print(ans)
