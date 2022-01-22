from itertools import groupby
from operator import mul
from functools import reduce


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


n = int(input())
s = list(input())

g = [[key, len(list(group))] for key, group in groupby(s)]

ans = 0
for v in g:
    if v[1] > 1:
        ans += combinations_count(v[1], 2)
print(ans)