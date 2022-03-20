from math import gcd

l, r = map(int, input().split())

ans = 0
for x in range(l, r + 1):
    if r - x < ans:
        break
    for y in range(r, l, -1):
        if gcd(x, y) == 1:
            ans = max(ans, y - x)
            break
print(ans)
