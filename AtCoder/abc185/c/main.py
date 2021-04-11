import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


L = int(input())

print(combinations_count(L - 1, 11))
