n, q = map(int, input().split())
cnt = [0] * n
for _ in range(q):
    e, x = map(int, input().split())
    x -= 1
    if e == 1:
        cnt[x] += 1
    elif e == 2:
        cnt[x] += 2
    else:
        if cnt[x] >= 2:
            print("Yes")
        else:
            print("No")
