t = int(input())
n = int(input())

cnt = [0] * (t + 10)
for i in range(n):
    l, r = map(int, input().split())
    cnt[l] += 1
    cnt[r] -= 1

cur = 0
for i in range(t):
    cur += cnt[i]
    print(cur)
