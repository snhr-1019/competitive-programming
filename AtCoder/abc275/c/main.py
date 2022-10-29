s = []

for _ in range(9):
    s.append(list(input()))

p = []
for i in range(9):
    for j in range(9):
        if s[i][j] == '#':
            p.append((i, j))


def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def is_square(a, b, c, d):
    dists = []
    dists.append(dist2(a, b))
    dists.append(dist2(b, c))
    dists.append(dist2(c, d))
    dists.append(dist2(d, a))
    dists.append(dist2(a, c))
    dists.append(dist2(b, d))
    dists.sort()

    return dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] and 2 * dists[0] == dists[4]


n = len(p)

ans = 0
for i in range(n - 3):
    for j in range(i + 1, n - 2):
        for k in range(j + 1, n - 1):
            for l in range(k + 1, n):
                if is_square(p[i], p[j], p[k], p[l]):
                    ans += 1
print(ans)
