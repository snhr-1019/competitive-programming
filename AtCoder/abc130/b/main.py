n, x = map(int, input().split())
l = list(map(int, input().split()))
cur = 0
ans = 1
for li in l:
    cur += li
    ans += (cur <= x)
print(ans)
