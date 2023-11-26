d = int(input())

INF = 10 ** 19
ans = INF

for x in range(1, 5 * 10 ** 6):
    if d - x ** 2 < 0:
        break
    y = int((d - x ** 2) ** 0.5)
    ans = min(ans, abs(x ** 2 + y ** 2 - d))
    y += 1
    ans = min(ans, abs(x ** 2 + y ** 2 - d))
print(ans)
