N, W = map(int, input().split())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))

AB.sort(reverse=True)

ans = 0
for ab in AB:
    a = ab[0]
    b = ab[1]
    weight = min(W, b)
    ans += a * weight
    W -= weight
print(ans)
