n, m = map(int, input().split())

INF = 10 ** 13
ans = INF

for a in range(1, 10 ** 7):
    b = -(-m // a)
    if a <= n and b <= n:
        ans = min(ans, a * b)
if ans == INF:
    print(-1)
else:
    print(ans)
