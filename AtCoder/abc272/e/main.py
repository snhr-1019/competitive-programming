import math

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
# cand[i]: i回目の操作で存在する非負整数のset
cand = [set() for _ in range(m + 1)]

# A[i]に対して
for i in range(1, n + 1):
    cnt = max(0, -(a[i] // i))
    while True:
        t = a[i] + cnt * i
        if t > n or cnt > m:
            break
        cand[cnt].add(a[i] + cnt * i)
        cnt += 1

for i in range(1, m + 1):
    for j in range(n + 1):
        if j not in cand[i]:
            print(j)
            break
