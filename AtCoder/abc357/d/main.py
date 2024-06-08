n = int(input())
l = len(str(n))
MOD = 998244353


def modpow(a, n):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % MOD
        a = a * a % MOD
        n >>= 1
    return res

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a):
    g, x, y = xgcd(a, MOD)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % MOD

ans = ((n * (modpow(10, n * l) - 1)) * modinv((modpow(10, l) - 1))) % MOD
print(ans)
