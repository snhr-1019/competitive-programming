p = int(input())

coins = []
f = 1
for i in range(1, 11):
    f *= i
    coins.append(f)
coins.sort(reverse=True)
ans = 0
for c in coins:
    n = min(100, p // c)
    ans += n
    p -= c * n
print(ans)
