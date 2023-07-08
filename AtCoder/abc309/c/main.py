from collections import defaultdict

n, k = map(int, input().split())

s = defaultdict(int)
st = 0
for _ in range(n):
    a, b = map(int, input().split())
    s[a + 1] -= b
    st += b

cur = st
if cur <= k:
    print(1)
    exit()
for i in sorted(s.keys()):
    cur += s[i]
    if cur <= k:
        print(i)
        break
