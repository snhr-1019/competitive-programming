import collections
from operator import mul
from functools import reduce


def comb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)

ans = comb(N, 2)
for cnt in c.values():
    if cnt > 1:
        ans -= comb(cnt, 2)
print(ans)
