n, k = map(int, input().split())

ans = 1
MOD = 10 ** 9 + 7


def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x, n // 2) ** 2 % MOD
    else:
        return x * power(x, (n - 1) // 2) ** 2 % MOD


if n == 1:
    ans = k
elif n == 2:
    ans = k * (k - 1)
else:
    ans = k * (k - 1) * power(k - 2, n - 2)
ans %= MOD
print(ans)
