from functools import lru_cache

x = int(input())
M = 998244353


@lru_cache
def f(x):
    if x <= 4:
        return x
    else:
        nxt1 = x // 2
        nxt2 = x - nxt1
        return f(nxt1) * f(nxt2) % M


print(f(x))
