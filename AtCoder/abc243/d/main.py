n, x = map(int, input().split())
s = input()

t = [s[0]]
for i in range(1, n):
    if len(t) != 0:
        prev = t[-1]
        nxt = s[i]
        if prev in ("R", "L") and nxt == "U":
            t.pop()
            continue
    t.append(s[i])

cur = x
for ti in t:
    if ti == "U":
        cur //= 2
    elif ti == "L":
        cur = cur * 2
    elif ti == "R":
        cur = cur * 2 + 1
print(cur)
