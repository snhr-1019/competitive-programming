n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (2 * 10 ** 5 + 10)

for i in range(n):
    cnt[a[i]] += 1


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


ans = 0

for i in range(n):
    for d in make_divisors(a[i]):
        m = a[i] // d
        ans += (cnt[d] * cnt[m])
print(ans)

