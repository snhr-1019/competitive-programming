from itertools import permutations

n, m = map(int, input().split())
s = [input() for _ in range(n)]


def ok(a, b):
    diff = 0
    for i in range(m):
        diff += (a[i] != b[i])
    return diff == 1


for t in permutations(s):
    if all(ok(t[i], t[i + 1]) for i in range(n - 1)):
        print("Yes")
        exit()
print("No")
