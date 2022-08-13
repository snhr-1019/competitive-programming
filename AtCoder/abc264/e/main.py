####
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


####

n, m, e = map(int, input().split())

uv = []
for _ in range(e):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uv.append([u, v])

q = int(input())

X = []
for _ in range(q):
    x = int(input())
    x -= 1
    X.append(x)
X.reverse()

set_x = set(X)

ans = []
uf = UnionFind(n + m)

for i in range(e):
    # イベントが起きない電線は最後まで生きてる
    if i not in set_x:
        uv_ = uv[i]
        uf.union(uv_[0], uv_[1])

cur = 0
is_ok = [False] * n
for c in range(n):
    for el in range(n, n + m):
        if uf.same(c, el) and not is_ok[c]:
            cur += 1
            is_ok[c] = True
ans.append(cur)

for ev in range(q):
    # イベントによって復活する電線
    uv_ = uv[X[ev]]
    uf.union(uv_[0], uv_[1])

    for c in range(n):
        if is_ok[c]:
            continue
        for el in range(n, n + m):
            if uf.same(c, el) and not is_ok[c]:
                cur += 1
                is_ok[c] = True
    ans.append(cur)

ans.reverse()
print(*ans[1:], sep="\n")
