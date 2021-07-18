from collections import defaultdict

n, k = map(int, input().split())
c = list(map(int, input().split()))

dic = defaultdict(int)

ans = 0
cnt = 0
for i in range(k):
    dic[c[i]] += 1
    if dic[c[i]] == 1:
        cnt += 1
ans = cnt

for i in range(n - k):
    dic[c[i]] -= 1
    if dic[c[i]] == 0:
        cnt -= 1
    dic[c[i + k]] += 1
    if dic[c[i + k]] == 1:
        cnt += 1
    ans = max(ans, cnt)
print(ans)
