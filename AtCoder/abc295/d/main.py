from collections import defaultdict

s = input()
n = len(s)
acc = [0] * (n + 1)
for i in range(n):
    c = int(s[i])
    acc[i + 1] = acc[i] ^ (1 << c)

cnt = defaultdict(int)
for acc_i in acc:
    cnt[acc_i] += 1

ans = 0
for v in cnt.values():
    ans += v * (v - 1) // 2
print(ans)
