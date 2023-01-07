t = int(input())
N = [int(input()) for _ in range(t)]


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def solve(n):
    p = 0
    q = 0
    for i in prime_list:
        if n % i == 0:
            if n % (i ** 2) == 0:
                p = i
                q = n // (p ** 2)
            else:
                q = i
                p = int((n // q) ** 0.5)
    print(p, q)


prime_list = primes(int(max(N) ** (1 / 3)))

for n in N:
    solve(n)
