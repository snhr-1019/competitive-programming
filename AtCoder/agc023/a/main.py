from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
acc = [0] * (n + 1)
for i in range(n):
    acc[i + 1] = acc[i] + a[i]

cnt = defaultdict(int)
for acc_i in acc:
    cnt[acc_i] += 1

ans = 0
for v in cnt.values():
    ans += v * (v - 1) // 2
print(ans)
