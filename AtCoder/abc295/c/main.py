from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
cnt = defaultdict(int)

for ai in a:
    cnt[ai] += 1

ans = 0
for k, v in cnt.items():
    ans += v // 2
print(ans)
