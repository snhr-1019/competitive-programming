from itertools import combinations

n, p, q = map(int, input().split())
a = list(map(lambda x: int(x) % p, input().split()))

ans = 0
for v in combinations(a, 5):
    if v[0] * v[1] % p * v[2] % p * v[3] % p * v[4] % p == q:
        ans += 1
print(ans)
