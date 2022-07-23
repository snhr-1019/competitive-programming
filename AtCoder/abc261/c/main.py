from collections import defaultdict

n = int(input())
cnt = defaultdict(int)

for _ in range(n):
    s = input()
    c = cnt[s]
    if c == 0:
        print(s)
    else:
        print(f"{s}({c})")
    cnt[s] += 1
