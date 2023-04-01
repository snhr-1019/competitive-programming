n, m = map(int, input().split())


def is_ok(t):
    for i in range(1, int(t ** 0.5) + 1):
        if t % i == 0 and i <= n and t // i <= n:
            return True
    return False


cur = m
while cur ** 0.5 <= n and cur <= n ** 2:
    if is_ok(cur):
        print(cur)
        exit()
    cur += 1
print(-1)
