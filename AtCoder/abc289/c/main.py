n, m = map(int, input().split())

s = [0] * m
for i in range(m):
    c = int(input())
    val = 0
    a = list(map(lambda x: int(x) - 1, input().split()))
    for j in range(c):
        val += 2 ** a[j]
    s[i] = val

ans = 0
for i in range(2 ** m):
    val = 0
    for j in range(m):
        if (i >> j) & 1:
            val |= s[j]
    if val == 2 ** n - 1:
        ans += 1
print(ans)
