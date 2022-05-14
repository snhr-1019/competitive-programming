n, w = map(int, input().split())
a = [0] + list(map(int, input().split()))

cand = set()
for x in range(n + 1):
    for y in range(n + 1):
        for z in range(n + 1):
            if (x + y != 0 and x == y) or (y + z != 0 and y == z) or (z + x != 0 and z == x) or (x + y + z == 0):
                continue
            if a[x] + a[y] + a[z] <= w:
                cand.add(a[x] + a[y] + a[z])
print(len(cand))
print(cand)
