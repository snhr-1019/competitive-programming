n = int(input())
a = list(map(int, input().split()))
ans = [a[0]]

for i in range(1, n):
    if a[i] - a[i - 1] > 1:
        for j in range(a[i - 1] + 1, a[i], 1):
            ans.append(j)
    elif a[i] - a[i - 1] < -1:
        for j in range(a[i - 1] - 1, a[i], -1):
            ans.append(j)
    ans.append(a[i])

print(*ans)
