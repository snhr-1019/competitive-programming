from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
cnt = defaultdict(int)
for i in range(n):
    cnt[a[i]] += 1

ans = 0
for vi, ci in cnt.items():
    for vj, cj in cnt.items():
        ans += (vi - vj) ** 2 * (ci * cj)
ans //= 2
print(ans)
