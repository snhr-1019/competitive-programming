N = int(input())

cur = 1
ans = 0
while cur <= N:
    s = cur
    v = N // cur
    e = min(N // v, N)
    ans += (e - s + 1) * v
    cur = e + 1
print(ans)
