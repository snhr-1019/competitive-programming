import bisect
from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

accum = [0] * (N + 1)
for i in range(N):
    accum[i + 1] = accum[i] + A[i]

ans = 0

cnt = defaultdict(list)

for i in range(N + 1):
    cnt[accum[i]].append(i)

ans = 0
for l in range(N):
    v = cnt[accum[l] + K]
    if not v:
        continue
    ans += len(v) - bisect.bisect_right(v, l)
print(ans)
