h, m = map(int, input().split())


def is_valid(a, b, c, d):
    h = int(a + c)
    m = int(b + d)
    return 0 <= h <= 23 and 0 <= m <= 59


while True:
    t = str(h).zfill(2)
    a = t[0]
    b = t[1]
    s = str(m).zfill(2)
    c = s[0]
    d = s[1]
    if is_valid(a, b, c, d):
        print(h, m)
        exit()

    m += 1
    if m == 60:
        m -= 60
        h += 1
        if h == 24:
            h -= 24
