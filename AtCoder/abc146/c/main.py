A, B, X = map(int, input().split())


def can_buy(n):
    return A * n + B * len(str(n)) <= X


ok = 0
ng = 10 ** 9 + 1

while ng - ok > 1:
    mid = (ok + ng) // 2
    if can_buy(mid):
        ok = mid
    else:
        ng = mid
print(ok)
