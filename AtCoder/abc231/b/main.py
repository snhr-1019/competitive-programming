from collections import defaultdict

N = int(input())
cnt = defaultdict(int)
for i in range(N):
    cnt[input()] += 1

print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[0][0])
