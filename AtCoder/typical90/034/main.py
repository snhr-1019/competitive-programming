from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

types = defaultdict(int)
cnt = 0
ans = 0
r = 0
for l in range(n):
    while r < n:
        if types[a[r]] == 0 and cnt == k:
            break
        if types[a[r]] == 0:
            cnt += 1
        types[a[r]] += 1
        r += 1
    ans = max(ans, r - l)
    if types[a[l]] == 1:
        cnt -= 1
    types[a[l]] -= 1
print(ans)
