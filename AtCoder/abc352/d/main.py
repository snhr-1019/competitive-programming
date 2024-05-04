from sortedcontainers import SortedSet

n, k = map(int, input().split())
p = list(map(int, input().split()))
pos = [-1] * (n + 1)
for i in range(n):
    pos[p[i]] = i

ans = 10 ** 18
s = SortedSet()
for i in range(1, k + 1):
    s.add(pos[i])
ans = min(ans, s[-1] - s[0])

for i in range(1, n - k + 1):
    s.remove(pos[i])
    s.add(pos[i + k])
    ans = min(ans, s[-1] - s[0])
print(ans)
