n, q = map(int, input().split())
follow = [[False] * n for _ in range(n)]

for i in range(q):
    s = list(map(int, input().split()))
    t = s[0]
    a = s[1] - 1
    if t == 1:
        b = s[2] - 1
        follow[a][b] = True
    elif t == 2:
        for i in range(n):
            if follow[i][a]:
                follow[a][i] = True
    elif t == 3:
        l = []
        for i in range(n):
            if follow[a][i]:
                for j in range(n):
                    if j != a and follow[i][j]:
                        l.append(j)
        for i in l:
            follow[a][i] = True

for i in range(n):
    print(*['Y' if f else 'N' for f in follow[i]], sep='')
