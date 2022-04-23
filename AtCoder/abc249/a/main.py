a, b, c, d, e, f, x = map(int, input().split())
y = x

takahashi = 0
while x > 0:
    t = min(x, a)
    takahashi += t * b
    x -= t
    x -= c

aoki = 0
while y > 0:
    t = min(y, d)
    aoki += t * e
    y -= t
    y -= f

if takahashi > aoki:
    print("Takahashi")
elif aoki > takahashi:
    print("Aoki")
else:
    print("Draw")
