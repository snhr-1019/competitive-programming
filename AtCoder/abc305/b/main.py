d = [3, 1, 4, 1, 5, 9]
p, q = input().split()
p = ord(p) - ord('A')
q = ord(q) - ord('A')
if p > q:
    p, q = q, p

ans = 0
for i in range(p, q):
    ans += d[i]
print(ans)
