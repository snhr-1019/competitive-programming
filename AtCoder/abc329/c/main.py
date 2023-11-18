from collections import defaultdict

n = int(input())
s = input()

cnt = [0] * n
dd = defaultdict(int)
for i in range(n):
    if i == 0:
        cnt[i] = 1
    else:
        if s[i] == s[i - 1]:
            cnt[i] = cnt[i - 1] + 1
        else:
            cnt[i] = 1

    dd[s[i]] = max(dd[s[i]], cnt[i])

ans = 0
for k, v in dd.items():
    ans += v
print(ans)
