n = int(input())
s = list(input())

q = int(input())

mode = 0
ex = set()
for i in range(q):
    t, x, c = input().split()
    t = int(t)
    x = int(x) - 1
    if t == 1:
        s[x] = c
        ex.add(x)
    elif t == 2:
        mode = 1
        ex = set()
    elif t == 3:
        mode = 2
        ex = set()

ans = []
for i in range(n):
    if mode == 0 or i in ex:
        ans.append(s[i])
    elif mode == 1:
        ans.append(s[i].lower())
    elif mode == 2:
        ans.append(s[i].upper())
print(*ans, sep='')
