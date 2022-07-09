from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def dist_2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def is_overlap(xyr_1, xyr_2):
    x1 = xyr_1[0]
    y1 = xyr_1[1]
    d1 = xyr_1[2]

    x2 = xyr_2[0]
    y2 = xyr_2[1]
    d2 = xyr_2[2]

    d_2 = dist_2(x1, y1, x2, y2)
    if d_2 < (d1 - d2) ** 2:
        return False
    if d_2 > (d1 + d2) ** 2:
        return False
    return True


n = int(input())
sx, sy, tx, ty = map(int, input().split())
xyr = []
for _ in range(n):
    xyr.append(list(map(int, input().split())))

uf = UnionFind(n)

for i in range(n):
    if dist_2(sx, sy, xyr[i][0], xyr[i][1]) == xyr[i][2] ** 2:
        s = i
    if dist_2(tx, ty, xyr[i][0], xyr[i][1]) == xyr[i][2] ** 2:
        t = i

for i in range(n - 1):
    for j in range(1, n):
        if is_overlap(xyr[i], xyr[j]):
            uf.union(i, j)

if uf.same(s, t):
    print("Yes")
else:
    print("No")
