N, Q = map(int, input().split())
front = [-1] * (N + 1)
back = [-1] * (N + 1)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        y = q[2]
        back[x] = y
        front[y] = x
    elif q[0] == 2:
        x = q[1]
        y = q[2]
        back[x] = -1
        front[y] = -1
    else:
        x = q[1]
        cur = x
        while front[cur] != -1:
            cur = front[cur]
        out = [cur]
        while back[cur] != -1:
            cur = back[cur]
            out.append(cur)
        print(len(out), *out)
