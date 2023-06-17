n = int(input())
a = list(map(int, input().split()))
cnt = [0] * (n + 1)

ans = []
for i in range(3 * n):
    cnt[a[i]] += 1
    if cnt[a[i]] == 2:
        ans.append(a[i])
print(*ans)
