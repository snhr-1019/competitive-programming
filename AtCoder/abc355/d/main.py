from sortedcontainers import SortedList

n = int(input())
l = [0] * n
r = [0] * n
ls = SortedList()
rs = SortedList()

for i in range(n):
    l[i], r[i] = map(int, input().split())
    ls.add(l[i])
    rs.add(r[i])

ans = 0
for i in range(n):
    a = n - ls.bisect_right(r[i])
    b = rs.bisect_left(l[i])
    ans += n - 1 - a - b
print(ans // 2)
