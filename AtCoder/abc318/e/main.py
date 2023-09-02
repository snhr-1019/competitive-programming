from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dd = defaultdict(list)
for i in range(n):
    dd[a[i]].append(i)

ans = 0

for v in dd.values():
    if len(v) == 1:
        continue

    for i in range(1, len(v)):
        ans += (v[i] - v[i - 1] - 1) * i * (len(v) - i)
print(ans)
