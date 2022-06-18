h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0

if h1 + h2 + h3 != w1 + w2 + w3:
    print(0)
    exit()

s = h1 + h2 + h3

ans = 0
for a in range(1, s):
    for b in range(1, s):
        if a + b > s:
            continue
        for d in range(1, s):
            for e in range(1, s):
                if d + e > s:
                    continue
                c = h1 - a - b
                f = h2 - d - e
                g = w1 - a - d
                h = w2 - b - e
                i = h3 - g - h
                if c <= 0 or f <= 0 or g <= 0 or g <= 0 or h <= 0 or i <= 0:
                    continue
                if c + f + i == w3:
                    ans += 1
print(ans)
