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


def getId(r, c):
    return W * r + c


H, W = map(int, input().split())
Q = int(input())

grid = [[0] * (W + 2) for _ in range(H + 2)]
uf = UnionFind((H + 2) * (W + 2))

for i in range(Q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        r, c = tmp[1:]
        grid[r][c] = 1
        if grid[r + 1][c] == 1:
            uf.union(getId(r, c), getId(r + 1, c))
        if grid[r - 1][c] == 1:
            uf.union(getId(r, c), getId(r - 1, c))
        if grid[r][c + 1] == 1:
            uf.union(getId(r, c), getId(r, c + 1))
        if grid[r][c - 1] == 1:
            uf.union(getId(r, c), getId(r, c - 1))
    else:
        ra, ca, rb, cb = tmp[1:]
        if grid[ra][ca] == 1 and grid[rb][cb] == 1 and uf.same(getId(ra, ca), getId(rb, cb)):
            print("Yes")
        else:
            print("No")
