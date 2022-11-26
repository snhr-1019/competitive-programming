a, b = map(int, input().split())


def calc(num):
    return a / (1 + num) ** 0.5


def is_ok(mid):
    if mid == 0:
        return True
    # 操作を行うことによって短縮できる秒数
    diff = calc(mid - 1) - calc(mid)
    cost = b
    # コストよりも短縮できる秒数の方が大きければメリットがある
    return cost <= diff


def binary_search(ok, ng):
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = binary_search(0, 10 ** 18 + 10)
print(b * ans + calc(ans))
