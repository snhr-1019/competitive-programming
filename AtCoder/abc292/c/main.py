n = int(input())


def count_divisors(m):
    ret = 0
    k = int((m ** 0.5))
    for i in range(1, k + 1):
        if m % i == 0:
            if m // i == i:
                ret += 1
            else:
                ret += 2
    return ret


ans = 0
for ab in range(1, n):
    cd = n - ab
    ans += count_divisors(ab) * count_divisors(cd)
print(ans)
