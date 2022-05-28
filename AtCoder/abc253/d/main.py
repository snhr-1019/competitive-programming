n, a, b = map(int, input().split())

if a > b:
    a, b = b, a


def calc(k):
    l = 0 if n < k else 1
    r = n // k
    return k * (l + r) * (r - l + 1) // 2


ans = n * (n + 1) // 2
ma = calc(a)
ans -= ma

if a != b and b % a != 0:
    mb = calc(b)
    ans -= mb

    mab = calc(a * b)
    ans += mab

print(ans)
