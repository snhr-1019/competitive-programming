import bisect

n = int(input())
s = list(input())

o = []
x = []
for i in range(len(s)):
    if s[i] == 'o':
        o.append(i)
    else:
        x.append(i)

ans = 0
for i in range(len(s)):
    if s[i] == 'o':
        t = bisect.bisect_right(x, i)
        if t < len(x):
            ans += n - x[t]
    else:
        t = bisect.bisect_right(o, i)
        if t < len(o):
            ans += n - o[t]
print(ans)