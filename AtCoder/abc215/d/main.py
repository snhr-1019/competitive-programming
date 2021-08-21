def factorization(n):
    ret = set()

    for p in range(2, n + 1):
        if p * p > n:
            break

        if n % p == 0:
            while n % p == 0:
                n //= p
            ret.add(p)

    if n > 1:
        ret.add(n)
    return ret


N, M = map(int, input().split())
A = list(map(int, input().split()))

primes = set()

for a in A:
    primes |= factorization(a)

ans = []
for i in range(1, M + 1):
    for p in primes:
        if i % p == 0:
            break
    else:
        ans.append(i)

print(len(ans))
print(*ans)