from collections import defaultdict

n = int(input())
a = {i: v for i, v in enumerate(list(map(int, input().split())))}
q = int(input())

base = 0
for _ in range(q):
    query = list(map(int, input().split()))
    t = query[0]
    if t == 1:
        base = query[1]
        a = defaultdict(int)
    elif t == 2:
        a[query[1] - 1] += query[2]
    else:
        print(base + a[query[1] - 1])
