n = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(d[i]):
        s = set(str(i + 1) + str(j + 1))
        ans += len(s) == 1
print(ans)
