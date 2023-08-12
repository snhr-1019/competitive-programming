n = int(input())
c = [0] * n
a = []

for i in range(n):
    c[i] = int(input())
    a.append(set(map(int, input().split())))

x = int(input())

ans = []
for i in range(n):
    if x in a[i]:
        ans.append((c[i], i))
ans.sort()

ans2 = []
for i in range(len(ans)):
    if i > 0 and ans[i][0] != ans[i - 1][0]:
        break
    ans2.append(ans[i][1] + 1)
print(len(ans2))
print(*ans2, sep=' ')
