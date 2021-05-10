from collections import Counter
from itertools import combinations
from math import factorial


def comb(n, r):
    return int(factorial(n) / factorial(r) / factorial(n - r))


N = int(input())
A = [int(s[-3:]) for s in input().split()]
c = Counter(A)

ans = 0
for cmb in combinations(c.keys(), 2):
    if (cmb[0] - cmb[1]) % 200 == 0:
        print(cmb)
        ans += comb(c[cmb[0]] + c[cmb[1]], 2)
print(ans)
