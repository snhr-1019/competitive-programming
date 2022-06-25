n = int(input())
s = list(map(int, list(input())))
w = list(map(int, input().split()))

t = []
cnt = 0
for i in range(n):
    t.append((w[i], s[i]))
    if s[i] == 1:
        cnt += 1
ans = cnt
t.sort()

for i in range(n):
    if t[i][1] == 1:
        cnt -= 1
    else:
        cnt += 1
    if i == n - 1 or (t[i][0] != t[i + 1][0]):
        ans = max(ans, cnt)
print(ans)
