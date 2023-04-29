from math import isqrt

n = int(input())

k = isqrt(n)

sieve = [True] * (k + 1)
sieve[0] = False
sieve[1] = False
primes = []
for p in range(2, k + 1):
    if not sieve[p]:
        continue
    primes.append(p)
    for j in range(p * 2, k + 1, p):
        sieve[j] = False

prefix_sum = [0] * (k + 1)
for i in range(1, k):
    prefix_sum[i] = prefix_sum[i - 1] + sieve[i]

ans = 0
for i in range(len(primes)):
    a = primes[i]
    if a > int(n ** (1 / 5)) + 1:
        break
    for j in range(i + 1, len(primes)):
        b = primes[j]
        if b > int(n ** (1 / 3)) + 1:
            break

        c_max = isqrt(n // (a * a * b))
        if b >= c_max:
            continue
        ans += prefix_sum[c_max] - prefix_sum[b]
print(ans)
