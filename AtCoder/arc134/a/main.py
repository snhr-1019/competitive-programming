import math

n, l, w = map(int, input().split())
a = list(map(int, input().split())) + [l]

right = 0
ans = 0
for i in range(n + 1):
    nxt = a[i]
    if right < nxt:
        cnt = int(math.ceil((nxt - right) / w))
        # print(nxt, right, cnt)
        ans += cnt
    right = nxt + w
print(ans)