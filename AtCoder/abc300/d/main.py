M = 3 * 10 ** 5  # > (10 ** 12 / 2 ** 2 / 3) ** 0.5 ≒ 288675 より、c <= M が常に成り立つ


def get_primes(n):
    prime = [True for _ in range(n + 1)]
    prime[0] = False
    prime[1] = False
    primes = []

    for i in range(n + 1):
        if prime[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                prime[j] = False

    return primes


n = int(input())

primes = get_primes(M)
ans = 0
l = len(primes)
for i in range(l):
    k = l - 1
    for j in range(i + 1, l):
        if j > k:
            break
        while j < k:
            v = primes[i] ** 2 * primes[j]
            if v > n:
                k -= 1
                continue
            v *= primes[k]
            if v > n:
                k -= 1
                continue
            v *= primes[k]
            if v > n:
                k -= 1
                continue
            break
        ans += k - j
print(ans)
