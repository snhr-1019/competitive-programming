import sys

sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.root[x] += self.root[y]
        self.root[y] = x

    def size(self, x):
        return -1 * self.root[self.find(x)]


union_find = UnionFind(n)

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    union_find.unite(a, b)

ans = 0
for i in range(n):
    ans = max(ans, union_find.size(i))

print(ans)
