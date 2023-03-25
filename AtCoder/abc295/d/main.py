from collections import defaultdict

s = input()
n = len(s)
acc = [[0] * 10 for _ in range(n + 1)]
for i in range(n):
    c = int(s[i])
    acc[i + 1] = acc[i][:]
    acc[i + 1][c] ^= 1

cnt = defaultdict(int)
for acc_i in acc:
    b = 0
    for i in range(10):
        b |= acc_i[i] << i
    cnt[b] += 1

ans = 0
for v in cnt.values():
    ans += v * (v - 1) // 2
print(ans)
