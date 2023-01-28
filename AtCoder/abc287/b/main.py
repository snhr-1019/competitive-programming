n, m = map(int, input().split())
s = []
t = set()
for _ in range(n):
    s.append(input())

for _ in range(m):
    t.add(input())

ans = 0
for si in s:
    if si[-3:] in t:
        ans += 1
print(ans)
