from collections import defaultdict

s = input()
cnt = defaultdict(int)

for c in s:
    cnt[c] += 1

print(max(cnt, key=lambda x: (cnt[x], -ord(x))))
