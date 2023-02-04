n, k = map(int, input().split())
a = list(map(int, input().split()))
q = int(input())


def solve(l, r):
    """
    l, rは半開区間
    """
    diff = 0
    d = [0] * (n + 10)
    for i in range(l, r):
        if i + k <= r:
            n_diff = - (a[i] + diff)
            d[i] = n_diff
            d[i + k] = -n_diff

        diff += d[i]
        if a[i] + diff != 0:
            print("No")
            return
    print("Yes")
    return


for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    solve(l, r)
