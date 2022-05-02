n = int(input())
s = set()
for a in range(2, 10**5+1):
    cur = a * a
    while cur <= n:
        s.add(cur)
        cur *= a
print(n - len(s))
