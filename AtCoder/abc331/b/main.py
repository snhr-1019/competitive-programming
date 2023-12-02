n, s, m, l = map(int, input().split())

ans = 10 ** 9
for sn in range(100):
    for mn in range(100):
        for ln in range(100):
            if n <= sn * 6 + mn * 8 + ln * 12:
                ans = min(ans, sn * s + mn * m + ln * l)
print(ans)
