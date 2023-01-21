n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
p -= 1
q -= 1
r -= 1
s -= 1

b = a[:]
b[p:q + 1] = a[r:s + 1]
b[r:s + 1] = a[p:q + 1]
print(*b)
