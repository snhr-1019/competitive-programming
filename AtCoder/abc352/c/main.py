n = int(input())
a = [0] * n
b = [0] * n
d = [0] * n
for i in range(n):
    ai, bi = map(int, input().split())
    a[i] = ai
    b[i] = bi
    d[i] = bi - ai
ans = sum(a) + max(d)
print(ans)
