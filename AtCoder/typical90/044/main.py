n, q = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
for i in range(q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1

    if t == 1:
        x = (x + start) % n
        y = (y + start) % n
        tmp = arr[x]
        arr[x] = arr[y]
        arr[y] = tmp
    elif t == 2:
        start -= 1
        start %= n
    else:
        print(arr[(x + start) % n])
