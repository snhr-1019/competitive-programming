import math

n = int(input())

p_max = 10 ** 6


def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


plist = get_sieve_of_eratosthenes(p_max)

cnt = 0
for q in plist:
    for p in plist:
        if p >= q or p * q ** 3 > n:
            break
        cnt += 1
print(cnt)
