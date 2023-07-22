n, d = map(int, input().split())
s = [list(input()) for _ in range(n)]

ans = 0
cur = 0
for i in range(d):
    if all([s[j][i] == 'o' for j in range(n)]):
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 0
print(ans)
