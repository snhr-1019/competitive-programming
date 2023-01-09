d = int(input())
n = int(input())

cnt = [0] * (d + 10)

for i in range(n):
    l, r = map(int, input().split())
    cnt[l] += 1
    cnt[r + 1] -= 1

cur = 0
for i in range(1, d + 1):
    cur += cnt[i]
    print(cur)
