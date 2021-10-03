P = int(input())

coins = []
f = 1
coins.append(1)
for i in range(2, 11):
    f *= i
    coins.append(f)
coins.sort(reverse=True)
ans = 0
for c in coins:
    if P >= c:
        P -= c
        ans += 1
print(ans)