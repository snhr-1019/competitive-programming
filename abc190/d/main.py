N = int(input())

primes = set()
f = 1
while f * f <= N:
    if N % f == 0:
        primes.add(f)
        primes.add(N // f)
    f += 1

ans = 0
for prime in primes:
    quotient = N // prime
    if quotient % 2 == 1:
        # 商が奇数なら作れる
        t = quotient // 2
        ans += 1

    if (prime // 2) + (prime // 2 + 1) == prime:
        # 商が偶数でも割る数が連続する数の和で表せるなら作れる
        ans += 1

print(ans)
