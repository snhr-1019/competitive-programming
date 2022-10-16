from collections import defaultdict
from bisect import bisect

h, w, r, c = map(int, input().split())
n = int(input())
r_dict = defaultdict(lambda: [0, w + 1])  # 便宜上、左右の端に壁を置く
c_dict = defaultdict(lambda: [0, h + 1])  # 便宜上、上下の端に壁を置く

for _ in range(n):
    ri, ci = map(int, input().split())
    r_dict[ri].append(ci)
    c_dict[ci].append(ri)

for v in r_dict.values():
    v.sort()

for v in c_dict.values():
    v.sort()

q = int(input())
for _ in range(q):
    d, l = input().split()
    l = int(l)
    if d == 'L':
        # いまより左にある最初の壁を探す
        b = bisect(r_dict[r], c) - 1
        c = max(r_dict[r][b] + 1, c - l)
    elif d == 'R':
        # いまより右にある最初の壁を探す
        b = bisect(r_dict[r], c)
        c = min(r_dict[r][b] - 1, c + l)
    elif d == 'U':
        # いまより上にある最初の壁を探す
        b = bisect(c_dict[c], r) - 1
        r = max(c_dict[c][b] + 1, r - l)
    elif d == 'D':
        # いまより下にある最初の壁を探す
        b = bisect(c_dict[c], r)
        r = min(c_dict[c][b] - 1, r + l)
    print(r, c)
