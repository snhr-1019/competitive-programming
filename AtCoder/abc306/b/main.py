a = list(map(int, input().split()))

ans = a[0]
base = 1

for i in range(1, 64):
    base *= 2
    ans += a[i] * base
print(ans)
