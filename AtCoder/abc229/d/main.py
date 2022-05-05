s = input()
k = int(input())
n = len(s)

# rはkを超えるか右端を超えてダメになった箇所
# 進めてからOKかどうか判定するので、この方がやりやすい
cnt = 0
r = 0
ans = 0
for l in range(n):
    while r < n and cnt + (s[r] == '.') <= k:
        cnt += (s[r] == '.')
        r += 1
    ans = max(ans, r - l)
    cnt -= (s[l] == '.')
print(ans)
