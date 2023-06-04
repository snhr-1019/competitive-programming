from collections import defaultdict
from bisect import bisect

w, h = map(int, input().split())
n = int(input())
cnt = defaultdict(int)

pq = []

for bi in range(n):
    pi, qi = map(int, input().split())
    pq.append((pi, qi))

A = int(input())
a = [0] + list(map(int, input().split()))
B = int(input())
b = [0] + list(map(int, input().split()))

BIAS = 10 ** 6
for pi, qi in pq:
    ai = bisect(a, pi) - 1
    bi = bisect(b, qi) - 1
    cnt[bi * BIAS + ai] += 1

mn = 10 ** 10
mx = -1

if len(cnt.keys()) < (A + 1) * (B + 1):
    mn = 0

mn = min(mn, min(cnt.values()))
mx = max(cnt.values())

print(mn, mx)
