from collections import defaultdict
import bisect

cnt = defaultdict(int)

N, Q = map(int, input().split())
A = list(map(int, input().split()))

for a in A:
    cnt[a] += 1

l = sorted(cnt.items(), key=lambda x: x[0], reverse=True)
cumsum = [0] * len(l)
cumsum[0] = l[0][1]

for i in range(1, len(l)):
    cumsum[i] = cumsum[i - 1] + l[i][1]
cumsum = [0] + cumsum
# print(cumsum)

sortedkey = sorted(list(cnt.keys()))

for i in range(Q):
    x = int(input())
    p = bisect.bisect_left(sortedkey, x)
    #print(sortedkey)
    #print(p)
    print(cumsum[len(l)-p])
