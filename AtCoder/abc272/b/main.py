from itertools import combinations

n, m = map(int, input().split())

all = dict()

for v in combinations(range(n), 2):
    all[v] = False

for _ in range(m):
    t = list(map(int, input().split()))
    k = map(lambda x: x - 1, t[1:])
    for v in combinations(k, 2):
        all[v] = True

for v in all.values():
    if not v:
        print("No")
        exit()
print("Yes")
