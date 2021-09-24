from collections import Counter

N = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return Counter(a)


ans = 0
for v in prime_factorize(N).items():
    cnt = v[1]
    for i in range(1, N):
        if cnt - i >= 0:
            cnt -= i
            ans += 1
        else:
            break
print(ans)
