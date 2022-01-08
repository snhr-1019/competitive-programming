n, k = map(int, input().split())


def a(n):
    s = map(int, list(str(n)))
    return (n + sum(s)) % 10 ** 5


if n == 0:
    print(0)
    exit()

cur = n
appeared = [[False, 0] for _ in range(10 ** 5 + 1)]
appeared[n] = [True, 0]

i = 0
shortcut = False
while i < k:
    cur = a(cur)
    if appeared[cur][0] and not shortcut:
        t = appeared[cur][1]
        l = i - t
        i += ((k - i) // l - 1) * l + 1
        shortcut = True
    else:
        appeared[cur][0] = True
        appeared[cur][1] = i
        i += 1
print(cur)
