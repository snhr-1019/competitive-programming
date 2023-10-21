n = int(input())

w = []
x = []
for _ in range(n):
    wi, xi = map(int, input().split())
    w.append(wi)
    x.append(xi)

ans = 0
for d in range(24):
    tmp = 0
    for i in range(n):
        if 9 <= (d + x[i]) % 24 < 18:
            tmp += w[i]
    ans = max(ans, tmp)
print(ans)
