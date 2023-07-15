n, m = map(int, input().split())

p = []
c = []
f = []

for _ in range(n):
    l = list(map(int, input().split()))
    p.append(l[0])
    c.append(l[1])
    f.append(set(l[2:]))


def is_ok(i, j):
    if not (p[i] >= p[j]):
        return False

    if not (len(f[i] - f[j]) == 0):
        return False

    if p[i] > p[j] or len(f[j] - f[i]) > 0:
        return True
    else:
        return False


for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if is_ok(i, j):
            print("Yes")
            exit()

print("No")
