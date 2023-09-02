n, d, p = map(int, input().split())
f = sorted(list(map(int, input().split())), reverse=True)
ans = sum(f)

for cnt in range(n // d + 1):
    s = sum(f[cnt * d:cnt * d + d])
    if s > p:
        ans += p - s
    else:
        break
print(ans)
