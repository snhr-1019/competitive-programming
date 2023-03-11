n = int(input())
a = [0] + list(map(int, input().split()))
called = [False] * (n + 1)

for i in range(1, n+1):
    if called[i]:
        continue
    called[a[i]] = True
ans = []
for i in range(1, n+1):
    if not called[i]:
        ans.append(i)
ans.sort()
print(len(ans))
print(*ans)
