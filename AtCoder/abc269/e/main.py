n = int(input())


def f(rc):
    l = 1
    r = n
    while r - l > 0:
        mid = (l + r) // 2
        if rc == 0:
            print("?", l, mid, 1, n)
        else:
            print("?", 1, n, l, mid)
        ret = int(input())
        if ret == mid - l + 1:
            # 右側に最後のルークはある
            l = mid + 1
        else:
            r = mid
    return l


i = f(0)
j = f(1)
print("!", i, j)
