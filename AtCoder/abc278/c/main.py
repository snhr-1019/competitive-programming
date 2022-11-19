from collections import defaultdict

n, q = map(int, input().split())
f = defaultdict(set)

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        f[a].add(b)
    elif t == 2:
        if b in f[a]:
            f[a].remove(b)
    else:
        if a in f[b] and b in f[a]:
            print("Yes")
        else:
            print("No")
